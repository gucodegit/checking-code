from typing import List

from fastapi import Depends, HTTPException

from checking_code.apps.students.managers import StudentsManager
from checking_code.apps.students.schemas import (
    CreateStudentSchema,
    StudentReturnData,
    UpdateStudentFieldsRequest,
)


class StudentsService:
    def __init__(self, manager: StudentsManager = Depends(StudentsManager)) -> None:
        self.manager = manager

    async def create_student(self, student: CreateStudentSchema) -> StudentReturnData:
        return await self.manager.create_student(student=student)

    async def get_student(self, id: int) -> StudentReturnData:
        return await self.manager.get_student(id=id)

    async def get_students(self) -> List[StudentReturnData]:
        return await self.manager.get_students()

    async def update_student_fields(
        self, id: int, data: UpdateStudentFieldsRequest
    ) -> StudentReturnData:
        payload = data.model_dump(exclude_unset=True)
        payload.pop("id", None)
        if not (payload):
            raise HTTPException(status_code=400, detail="No fields to update")
        return await self.manager.update_student_fields(id=id, **payload)

    async def delete_student(self, id: int) -> StudentReturnData:
        return await self.manager.delete_student(id=id)
