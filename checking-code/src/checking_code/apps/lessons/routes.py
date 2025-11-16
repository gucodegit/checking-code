from typing import List

from fastapi import APIRouter, Depends, status

from checking_code.apps.lessons.services import LessonsService
from checking_code.apps.lessons.schemas import (
    CreateLessonSchema,
    LessonReturnData,
    UpdateLessonFieldRequests,
)


lessons_router = APIRouter(prefix="/lessons", tags=["Lessons"])


@lessons_router.post(
    path="/",
    response_model=LessonReturnData,
    status_code=status.HTTP_201_CREATED,
)
async def create_lesson(
    lesson: CreateLessonSchema, service: LessonsService = Depends(LessonsService)
) -> LessonReturnData:
    return await service.create_lesson(lesson=lesson)


@lessons_router.get(
    path="/{id}",
    response_model=LessonReturnData,
    status_code=status.HTTP_200_OK,
)
async def get_lesson(
    id: int, service: LessonsService = Depends(LessonsService)
) -> LessonReturnData:
    return await service.get_lesson(id=id)


@lessons_router.get(
    path="/",
    response_model=List[LessonReturnData],
    status_code=status.HTTP_200_OK,
)
async def get_lessons(
    service: LessonsService = Depends(LessonsService),
) -> List[LessonReturnData]:
    return await service.get_lessons()


@lessons_router.patch(
    path="/{id}",
    response_model=LessonReturnData,
    status_code=status.HTTP_200_OK,
)
async def update_lesson_fields(
    id: int,
    data: UpdateLessonFieldRequests,
    service: LessonsService = Depends(LessonsService),
) -> LessonReturnData:
    return await service.update_lesson_fields(id=id, data=data)


@lessons_router.delete(
    path="/{id}",
    response_model=LessonReturnData,
    status_code=status.HTTP_200_OK,
)
async def delete_lesson(
    id: int,
    service: LessonsService = Depends(LessonsService),
) -> LessonReturnData:
    return await service.delete_lesson(id=id)
