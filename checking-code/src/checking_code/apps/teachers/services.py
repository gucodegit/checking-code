from typing import List

from fastapi import Depends, HTTPException

from checking_code.apps.teachers.managers import TeachersManager
from checking_code.apps.teachers.schemas import (
    CreateTeacherSchema,
    TeacherReturnData,
    UpdateTeacherFieldRequest,
)


class TeachersService:
    def __init__(self, manager: TeachersManager = Depends(TeachersManager)) -> None:
        self.manager = manager

    async def create_teacher(self, teacher: CreateTeacherSchema) -> TeacherReturnData:
        return await self.manager.create_teacher(teacher=teacher)

    async def get_teacher(self, id: int) -> TeacherReturnData:
        return await self.manager.get_teacher(id=id)

    async def get_teachers(self) -> List[TeacherReturnData]:
        return await self.manager.get_teachers()

    async def update_teacher_fields(
        self, id: int, data: UpdateTeacherFieldRequest
    ) -> TeacherReturnData:
        payload = data.model_dump(exclude_unset=True)
        payload.pop("id", None)
        if not (payload):
            raise HTTPException(400, "No fields to update")
        return await self.manager.update_teacher_fields(id=id, **payload)

    async def delete_teacher(self, id: int) -> TeacherReturnData:
        return await self.manager.delete_teacher(id=id)
