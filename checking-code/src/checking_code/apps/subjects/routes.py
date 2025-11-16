from typing import List

from fastapi import APIRouter, Depends, status

from checking_code.apps.subjects.services import SubjectsService
from checking_code.apps.subjects.schemas import (
    CreateSubjectSchema,
    SubjectReturnData,
    UpdateSubjectFieldsRequest,
)


subjects_router = APIRouter(prefix="/subjects", tags=["Subjects"])


@subjects_router.post(
    path="/",
    response_model=SubjectReturnData,
    status_code=status.HTTP_201_CREATED,
)
async def create_subject(
    subject: CreateSubjectSchema, service: SubjectsService = Depends(SubjectsService)
) -> SubjectReturnData:
    return await service.create_subject(subject=subject)


@subjects_router.get(
    path="/{id}",
    response_model=SubjectReturnData,
    status_code=status.HTTP_200_OK,
)
async def get_subject(
    id: int, service: SubjectsService = Depends(SubjectsService)
) -> SubjectReturnData:
    return await service.get_subject(id=id)


@subjects_router.get(
    path="/",
    response_model=List[SubjectReturnData],
    status_code=status.HTTP_200_OK,
)
async def get_subjects(
    service: SubjectsService = Depends(SubjectsService),
) -> List[SubjectReturnData]:
    return await service.get_subjects()


@subjects_router.patch(
    path="/{id}",
    response_model=SubjectReturnData,
    status_code=status.HTTP_200_OK,
)
async def update_subject_fields(
    id: int,
    data: UpdateSubjectFieldsRequest,
    service: SubjectsService = Depends(SubjectsService),
) -> SubjectReturnData:
    return await service.update_subject_fields(id=id, data=data)


@subjects_router.delete(
    path="/{id}",
    response_model=SubjectReturnData,
    status_code=status.HTTP_200_OK,
)
async def delete_subject(
    id: int,
    service: SubjectsService = Depends(SubjectsService),
) -> SubjectReturnData:
    return await service.delete_subject(id=id)
