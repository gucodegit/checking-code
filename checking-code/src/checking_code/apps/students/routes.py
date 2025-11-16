from typing import List

from fastapi import APIRouter, Depends, status

from checking_code.apps.students.services import StudentsService
from checking_code.apps.students.schemas import (
    CreateStudentSchema,
    StudentReturnData,
    UpdateStudentFieldsRequest,
)


students_router = APIRouter(prefix="/students", tags=["Students"])


@students_router.post(
    path="/",
    response_model=StudentReturnData,
    status_code=status.HTTP_201_CREATED,
)
async def create_student(
    student: CreateStudentSchema, service: StudentsService = Depends(StudentsService)
) -> StudentReturnData:
    return await service.create_student(student=student)


@students_router.get(
    path="/{id}",
    response_model=StudentReturnData,
    status_code=status.HTTP_200_OK,
)
async def get_student(
    id: int, service: StudentsService = Depends(StudentsService)
) -> StudentReturnData:
    return await service.get_student(id=id)


@students_router.get(
    path="/",
    response_model=List[StudentReturnData],
    status_code=status.HTTP_200_OK,
)
async def get_students(
    service: StudentsService = Depends(StudentsService),
) -> List[StudentReturnData]:
    return await service.get_students()


@students_router.patch(
    path="/{id}",
    response_model=StudentReturnData,
    status_code=status.HTTP_200_OK,
)
async def update_student_fields(
    id: int,
    data: UpdateStudentFieldsRequest,
    service: StudentsService = Depends(StudentsService),
) -> StudentReturnData:
    return await service.update_student_fields(id=id, data=data)


@students_router.delete(
    path="/{id}",
    response_model=StudentReturnData,
    status_code=status.HTTP_200_OK,
)
async def delete_student(
    id: int,
    service: StudentsService = Depends(StudentsService),
) -> StudentReturnData:
    return await service.delete_student(id=id)
