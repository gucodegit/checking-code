from typing import List, Any

from fastapi import Depends, HTTPException
from sqlalchemy import insert, select, update, delete
from sqlalchemy.exc import IntegrityError

from checking_code.core.core_dependency.db_dependency import DBDependency
from checking_code.database.models import Teachers
from checking_code.apps.teachers.schemas import CreateTeacherSchema, TeacherReturnData


class TeachersManager:
    def __init__(self, db: DBDependency = Depends(DBDependency)) -> None:
        self.db = db
        self.model = Teachers

    async def create_teacher(self, teacher: CreateTeacherSchema) -> TeacherReturnData:
        async with self.db.get_session() as session:
            query = (
                insert(self.model).values(**teacher.model_dump()).returning(self.model)
            )
            try:
                result = await session.execute(query)
            except IntegrityError:
                raise HTTPException(status_code=400, detail="Teacher already exists")
            await session.commit()
            teacher_data = result.scalar_one()
            return TeacherReturnData.model_validate(teacher_data, from_attributes=True)

    async def get_teacher(self, id: int) -> TeacherReturnData:
        async with self.db.get_session() as session:
            query = select(self.model).where(self.model.id == id)
            result = await session.execute(query)
            teacher_data = result.scalar_one_or_none()
            if not (teacher_data):
                raise HTTPException(status_code=404, detail="Teacher not found")
            return TeacherReturnData.model_validate(teacher_data, from_attributes=True)

    async def get_teachers(self) -> List[TeacherReturnData]:
        async with self.db.get_session() as session:
            query = select(self.model)
            result = await session.execute(query)
            teachers_data = result.scalars().all()
            if not (teachers_data):
                raise HTTPException(status_code=404, detail="Teachers not found")
            return [
                TeacherReturnData.model_validate(teacher, from_attributes=True)
                for teacher in teachers_data
            ]

    async def update_teacher_fields(self, id: int, **kwargs: Any) -> TeacherReturnData:
        async with self.db.get_session() as session:
            query = (
                update(self.model)
                .where(self.model.id == id)
                .values(**kwargs)
                .returning(self.model)
            )
            try:
                result = await session.execute(query)
            except IntegrityError:
                raise HTTPException(status_code=400, detail="Teacher already exists")
            await session.commit()
            teacher_data = result.scalar_one_or_none()
            if not (teacher_data):
                raise HTTPException(status_code=404, detail="Teacher not found")
            return TeacherReturnData.model_validate(teacher_data, from_attributes=True)

    async def delete_teacher(self, id: int) -> TeacherReturnData:
        async with self.db.get_session() as session:
            query = delete(self.model).where(self.model.id == id).returning(self.model)
            result = await session.execute(query)
            await session.commit()
            teacher_data = result.scalar_one_or_none()
            if not (teacher_data):
                raise HTTPException(status_code=404, detail="Teacher not found")
            return TeacherReturnData.model_validate(teacher_data, from_attributes=True)
