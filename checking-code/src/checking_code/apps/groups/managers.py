from typing import List, Any

from fastapi import Depends, HTTPException
from sqlalchemy import insert, select, update, delete
from sqlalchemy.exc import IntegrityError

from checking_code.core.core_dependency.db_dependency import DBDependency
from checking_code.database.models import Groups
from checking_code.apps.groups.schemas import (
    CreateGroupSchema,
    GroupReturnData,
)


class GroupsManager:
    def __init__(self, db: DBDependency = Depends(DBDependency)) -> None:
        self.db = db
        self.model = Groups

    async def create_group(self, group: CreateGroupSchema) -> GroupReturnData:
        async with self.db.get_session() as session:
            query = (
                insert(self.model).values(**group.model_dump()).returning(self.model)
            )
            try:
                result = await session.execute(query)
            except IntegrityError:
                raise HTTPException(status_code=400, detail="Invalid data")
            await session.commit()
            group_data = result.scalar_one()
            return GroupReturnData.model_validate(group_data, from_attributes=True)

    async def get_group(self, id: int) -> GroupReturnData:
        async with self.db.get_session() as session:
            query = select(self.model).where(self.model.id == id)
            result = await session.execute(query)
            group_data = result.scalar_one_or_none()
            if not (group_data):
                raise HTTPException(status_code=404, detail="Group not found")
            return GroupReturnData.model_validate(group_data, from_attributes=True)

    async def get_groups(self) -> List[GroupReturnData]:
        async with self.db.get_session() as session:
            query = select(self.model)
            result = await session.execute(query)
            groups_data = result.scalars().all()
            if not (groups_data):
                raise HTTPException(status_code=404, detail="Groups not found")
            return [
                GroupReturnData.model_validate(group, from_attributes=True)
                for group in groups_data
            ]

    async def update_group_fields(self, id: int, **kwargs: Any) -> GroupReturnData:
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
            group_data = result.scalar_one_or_none()
            if not (group_data):
                raise HTTPException(status_code=404, detail="Group not found")
            return GroupReturnData.model_validate(group_data, from_attributes=True)

    async def delete_group(self, id: int) -> GroupReturnData:
        async with self.db.get_session() as session:
            query = delete(self.model).where(self.model.id == id).returning(self.model)
            result = await session.execute(query)
            await session.commit()
            group_data = result.scalar_one_or_none()
            if not (group_data):
                raise HTTPException(status_code=404, detail="Group not found")
            return GroupReturnData.model_validate(group_data, from_attributes=True)
