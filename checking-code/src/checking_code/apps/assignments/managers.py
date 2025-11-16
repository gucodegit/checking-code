from typing import List, Any

from fastapi import Depends, HTTPException
from sqlalchemy import insert, select, update, delete
from sqlalchemy.exc import IntegrityError

from checking_code.core.core_dependency.db_dependency import DBDependency
from checking_code.database.models import Assignments
from checking_code.apps.assignments.schemas import (
    CreateAssignmentSchema,
    AssignmentReturnData,
)


class AssignmentsManager:
    def __init__(self, db: DBDependency = Depends(DBDependency)) -> None:
        self.db = db
        self.model = Assignments

    async def create_assignment(
        self, assignment: CreateAssignmentSchema
    ) -> AssignmentReturnData:
        async with self.db.get_session() as session:
            query = (
                insert(self.model)
                .values(**assignment.model_dump())
                .returning(self.model)
            )
            try:
                result = await session.execute(query)
            except IntegrityError:
                raise HTTPException(status_code=400, detail="Invalid data")
            await session.commit()
            assignment_data = result.scalar_one()
            return AssignmentReturnData.model_validate(
                assignment_data, from_attributes=True
            )

    async def get_assignment(self, id: int) -> AssignmentReturnData:
        async with self.db.get_session() as session:
            query = select(self.model).where(self.model.id == id)
            result = await session.execute(query)
            assignment_data = result.scalar_one_or_none()
            if not (assignment_data):
                raise HTTPException(status_code=404, detail="Assignment not found")
            return AssignmentReturnData.model_validate(
                assignment_data, from_attributes=True
            )

    async def get_assignments(self) -> List[AssignmentReturnData]:
        async with self.db.get_session() as session:
            query = select(self.model)
            result = await session.execute(query)
            assignments_data = result.scalars().all()
            if not (assignments_data):
                raise HTTPException(status_code=404, detail="Assignments not found")
            return [
                AssignmentReturnData.model_validate(assignment, from_attributes=True)
                for assignment in assignments_data
            ]

    async def update_assignment_fields(
        self, id: int, **kwargs: Any
    ) -> AssignmentReturnData:
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
            assignment_data = result.scalar_one_or_none()
            if not (assignment_data):
                raise HTTPException(status_code=404, detail="Assignment not found")
            return AssignmentReturnData.model_validate(
                assignment_data, from_attributes=True
            )

    async def delete_assignment(self, id: int) -> AssignmentReturnData:
        async with self.db.get_session() as session:
            query = delete(self.model).where(self.model.id == id).returning(self.model)
            result = await session.execute(query)
            await session.commit()
            assignment_data = result.scalar_one_or_none()
            if not (assignment_data):
                raise HTTPException(status_code=404, detail="assignment not found")
            return AssignmentReturnData.model_validate(
                assignment_data, from_attributes=True
            )
