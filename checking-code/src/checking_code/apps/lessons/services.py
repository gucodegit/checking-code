from typing import List

from fastapi import Depends, HTTPException

from checking_code.apps.lessons.managers import LessonsManager
from checking_code.apps.lessons.schemas import (
    CreateLessonSchema,
    LessonReturnData,
    UpdateLessonFieldRequests,
)


class LessonsService:
    def __init__(self, manager: LessonsManager = Depends(LessonsManager)) -> None:
        self.manager = manager

    async def create_lesson(self, lesson: CreateLessonSchema) -> LessonReturnData:
        return await self.manager.create_lesson(lesson=lesson)

    async def get_lesson(self, id: int) -> LessonReturnData:
        return await self.manager.get_lesson(id=id)

    async def get_lessons(self) -> List[LessonReturnData]:
        return await self.manager.get_lessons()

    async def update_lesson_fields(
        self, id: int, data: UpdateLessonFieldRequests
    ) -> LessonReturnData:
        payload = data.model_dump(exclude_unset=True)
        payload.pop("id", None)
        if not (payload):
            raise HTTPException(status_code=400, detail="No fields to update")
        return await self.manager.update_lesson_fields(id=id, **payload)

    async def delete_lesson(self, id: int) -> LessonReturnData:
        return await self.manager.delete_lesson(id=id)
