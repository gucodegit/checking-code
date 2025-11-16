from typing import List

from fastapi import Depends, HTTPException

from checking_code.apps.groups.managers import GroupsManager
from checking_code.apps.groups.schemas import (
    CreateGroupSchema,
    GroupReturnData,
    UpdateGroupFieldsRequest,
)


class GroupsService:
    def __init__(self, manager: GroupsManager = Depends(GroupsManager)) -> None:
        self.manager = manager

    async def create_group(self, group: CreateGroupSchema) -> GroupReturnData:
        return await self.manager.create_group(group=group)

    async def get_group(self, id: int) -> GroupReturnData:
        return await self.manager.get_group(id=id)

    async def get_groups(self) -> List[GroupReturnData]:
        return await self.manager.get_groups()

    async def update_group_fields(
        self, id: int, data: UpdateGroupFieldsRequest
    ) -> GroupReturnData:
        payload = data.model_dump(exclude_unset=True)
        payload.pop("id", None)
        if not (payload):
            raise HTTPException(status_code=400, detail="No fields to update")
        return await self.manager.update_group_fields(id=id, **payload)

    async def delete_group(self, id: int) -> GroupReturnData:
        return await self.manager.delete_group(id=id)
