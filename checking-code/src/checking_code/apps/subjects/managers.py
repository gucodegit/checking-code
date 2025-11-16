from typing import List, Any

from fastapi import Depends, HTTPException
from sqlalchemy import insert, select, update, delete
from sqlalchemy.exc import IntegrityError

from checking_code.core.core_dependency.db_dependency import DBDependency
from checking_code.database.models import Subjects
from checking_code.apps.subjects.schemas import CreateSubjectSchema, SubjectReturnData


class SubjectsManager:
    def __init__(self, db: DBDependency = Depends(DBDependency)) -> None:
        self.db = db
        self.model = Subjects

    async def create_subject(self, subject: CreateSubjectSchema) -> SubjectReturnData:
        async with self.db.get_session() as session:
            query = (
                insert(self.model).values(**subject.model_dump()).returning(self.model)
            )
            try:
                result = await session.execute(query)
            except IntegrityError:
                raise HTTPException(status_code=400, detail="Invalid data")
            await session.commit()
            subject_data = result.scalar_one()
            return SubjectReturnData.model_validate(subject_data, from_attributes=True)

    async def get_subject(self, id: int) -> SubjectReturnData:
        async with self.db.get_session() as session:
            query = select(self.model).where(self.model.id == id)
            result = await session.execute(query)
            subject_data = result.scalar_one_or_none()
            if not (subject_data):
                raise HTTPException(status_code=404, detail="Subject not found")
            return SubjectReturnData.model_validate(subject_data, from_attributes=True)

    async def get_subjects(self) -> List[SubjectReturnData]:
        async with self.db.get_session() as session:
            query = select(self.model)
            result = await session.execute(query)
            subjects_data = result.scalars().all()
            if not (subjects_data):
                raise HTTPException(status_code=404, detail="Subjects not found")
            return [
                SubjectReturnData.model_validate(subject, from_attributes=True)
                for subject in subjects_data
            ]

    async def update_subject_fields(self, id: int, **kwargs: Any) -> SubjectReturnData:
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
            subject_data = result.scalar_one_or_none()
            if not (subject_data):
                raise HTTPException(status_code=404, detail="Subject not found")
            return SubjectReturnData.model_validate(subject_data, from_attributes=True)

    async def delete_subject(self, id: int) -> SubjectReturnData:
        async with self.db.get_session() as session:
            query = delete(self.model).where(self.model.id == id).returning(self.model)
            result = await session.execute(query)
            await session.commit()
            subject_data = result.scalar_one_or_none()
            if not (subject_data):
                raise HTTPException(status_code=404, detail="Subject not found")
            return SubjectReturnData.model_validate(subject_data, from_attributes=True)
