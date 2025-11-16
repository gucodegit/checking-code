from typing import List, Any

from fastapi import Depends, HTTPException
from sqlalchemy import insert, select, update, delete
from sqlalchemy.exc import IntegrityError

from checking_code.core.core_dependency.db_dependency import DBDependency
from checking_code.database.models import Students
from checking_code.apps.students.schemas import CreateStudentSchema, StudentReturnData


class StudentsManager:
    def __init__(self, db: DBDependency = Depends(DBDependency)) -> None:
        self.db = db
        self.model = Students

    async def create_student(self, student: CreateStudentSchema) -> StudentReturnData:
        async with self.db.get_session() as session:
            query = (
                insert(self.model).values(**student.model_dump()).returning(self.model)
            )
            try:
                result = await session.execute(query)
            except IntegrityError:
                raise HTTPException(status_code=400, detail="Invalid data")
            await session.commit()
            student_data = result.scalar_one()
            return StudentReturnData.model_validate(student_data, from_attributes=True)

    async def get_student(self, id: int) -> StudentReturnData:
        async with self.db.get_session() as session:
            query = select(self.model).where(self.model.id == id)
            result = await session.execute(query)
            student_data = result.scalar_one_or_none()
            if not (student_data):
                raise HTTPException(status_code=404, detail="Student not found")
            return StudentReturnData.model_validate(student_data, from_attributes=True)

    async def get_students(self) -> List[StudentReturnData]:
        async with self.db.get_session() as session:
            query = select(self.model)
            result = await session.execute(query)
            students_data = result.scalars().all()
            if not (students_data):
                raise HTTPException(status_code=404, detail="Students not found")
            return [
                StudentReturnData.model_validate(student, from_attributes=True)
                for student in students_data
            ]

    async def update_student_fields(self, id: int, **kwargs: Any) -> StudentReturnData:
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
                raise HTTPException(status_code=400, detail="Invalid data")
            await session.commit()
            student_data = result.scalar_one_or_none()
            if not (student_data):
                raise HTTPException(status_code=404, detail="Student not found")
            return StudentReturnData.model_validate(student_data, from_attributes=True)

    async def delete_student(self, id: int) -> StudentReturnData:
        async with self.db.get_session() as session:
            query = delete(self.model).where(self.model.id == id).returning(self.model)
            result = await session.execute(query)
            await session.commit()
            student_data = result.scalar_one_or_none()
            if not (student_data):
                raise HTTPException(status_code=404, detail="Student not found")
            return StudentReturnData.model_validate(student_data, from_attributes=True)
