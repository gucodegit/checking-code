from typing import List, Annotated

from fastapi import APIRouter, Depends, status, HTTPException

from checking_code.apps.assignments.services import assignmentsService
from checking_code.apps.assignments.schemas import (
    CreateAssignmentSchema,
    AssignmentReturnData,
    UpdateAssignmentFieldsRequest,
)
from checking_code.apps.auth.depends import get_current_user
from checking_code.apps.auth.schemas import GetAuthSchema

assignments_router = APIRouter(prefix="/assignments", tags=["Assignments"])


@assignments_router.post(
    path="/",
    response_model=AssignmentReturnData,
    status_code=status.HTTP_201_CREATED,
)
async def create_assignment(
    user: Annotated[GetAuthSchema, Depends(get_current_user)],
    assignment: CreateAssignmentSchema,
    service: assignmentsService = Depends(assignmentsService),
) -> AssignmentReturnData:
    if user.user_type != "teacher":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access denied"
        )
    return await service.create_assignment(assignment=assignment)


@assignments_router.get(
    path="/{id}",
    response_model=AssignmentReturnData,
    status_code=status.HTTP_200_OK,
)
async def get_assignment(
    id: int, service: assignmentsService = Depends(assignmentsService)
) -> AssignmentReturnData:
    return await service.get_assignment(id=id)


@assignments_router.get(
    path="/",
    response_model=List[AssignmentReturnData],
    status_code=status.HTTP_200_OK,
)
async def get_assignments(
    service: assignmentsService = Depends(assignmentsService),
) -> List[AssignmentReturnData]:
    return await service.get_assignments()


@assignments_router.patch(
    path="/{id}",
    response_model=AssignmentReturnData,
    status_code=status.HTTP_200_OK,
)
async def update_assignment_fields(
    id: int,
    data: UpdateAssignmentFieldsRequest,
    service: assignmentsService = Depends(assignmentsService),
) -> AssignmentReturnData:
    return await service.update_assignment_fields(id=id, data=data)


@assignments_router.delete(
    path="/{id}",
    response_model=AssignmentReturnData,
    status_code=status.HTTP_200_OK,
)
async def delete_assignment(
    user: Annotated[GetAuthSchema, Depends(get_current_user)],
    id: int,
    service: assignmentsService = Depends(assignmentsService),
) -> AssignmentReturnData:
    if user.user_type != "teacher":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access denied"
        )
    return await service.delete_assignment(id=id)
