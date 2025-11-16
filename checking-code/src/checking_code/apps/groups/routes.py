from typing import List

from fastapi import APIRouter, Depends, status

from checking_code.apps.groups.services import GroupsService
from checking_code.apps.groups.schemas import (
    CreateGroupSchema,
    GroupReturnData,
    UpdateGroupFieldsRequest,
)


groups_router = APIRouter(prefix="/groups", tags=["Groups"])


@groups_router.post(
    path="/",
    response_model=GroupReturnData,
    status_code=status.HTTP_201_CREATED,
)
async def create_group(
    group: CreateGroupSchema, service: GroupsService = Depends(GroupsService)
) -> GroupReturnData:
    return await service.create_group(group=group)


@groups_router.get(
    path="/{id}",
    response_model=GroupReturnData,
    status_code=status.HTTP_200_OK,
)
async def get_group(
    id: int, service: GroupsService = Depends(GroupsService)
) -> GroupReturnData:
    return await service.get_group(id=id)


@groups_router.get(
    path="/",
    response_model=List[GroupReturnData],
    status_code=status.HTTP_200_OK,
)
async def get_groups(
    service: GroupsService = Depends(GroupsService),
) -> List[GroupReturnData]:
    return await service.get_groups()


@groups_router.patch(
    path="/{id}",
    response_model=GroupReturnData,
    status_code=status.HTTP_200_OK,
)
async def update_group_fields(
    id: int,
    data: UpdateGroupFieldsRequest,
    service: GroupsService = Depends(GroupsService),
) -> GroupReturnData:
    return await service.update_group_fields(id=id, data=data)


@groups_router.delete(
    path="/{id}",
    response_model=GroupReturnData,
    status_code=status.HTTP_200_OK,
)
async def delete_group(
    id: int, service: GroupsService = Depends(GroupsService)
) -> GroupReturnData:
    return await service.delete_group(id=id)
