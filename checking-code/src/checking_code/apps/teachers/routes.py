from typing import List

from fastapi import APIRouter, Depends, status

from checking_code.apps.teachers.services import TeachersService
from checking_code.apps.teachers.schemas import (
    CreateTeacherSchema,
    TeacherReturnData,
    UpdateTeacherFieldRequest,
)


teachers_router = APIRouter(prefix="/teachers", tags=["Teachers"])


@teachers_router.post(
    path="/",
    response_model=TeacherReturnData,
    status_code=status.HTTP_201_CREATED,
)
async def create_teacher(
    teacher: CreateTeacherSchema, service: TeachersService = Depends(TeachersService)
) -> TeacherReturnData:
    return await service.create_teacher(teacher=teacher)


@teachers_router.get(
    path="/{id}",
    response_model=TeacherReturnData,
    status_code=status.HTTP_200_OK,
)
async def get_teacher(
    id: int, service: TeachersService = Depends(TeachersService)
) -> TeacherReturnData:
    return await service.get_teacher(id=id)


@teachers_router.get(
    path="/",
    response_model=List[TeacherReturnData],
    status_code=status.HTTP_200_OK,
)
async def get_teachers(
    service: TeachersService = Depends(TeachersService),
) -> List[TeacherReturnData]:
    return await service.get_teachers()


@teachers_router.patch(
    path="/{id}",
    response_model=TeacherReturnData,
    status_code=status.HTTP_200_OK,
)
async def update_teacher_fields(
    id: int,
    data: UpdateTeacherFieldRequest,
    service: TeachersService = Depends(TeachersService),
) -> TeacherReturnData:
    return await service.update_teacher_fields(id=id, data=data)


@teachers_router.delete(
    path="/{id}",
    response_model=TeacherReturnData,
    status_code=status.HTTP_200_OK,
)
async def delete_teacher(
    id: int,
    service: TeachersService = Depends(TeachersService),
) -> TeacherReturnData:
    return await service.delete_teacher(id=id)
