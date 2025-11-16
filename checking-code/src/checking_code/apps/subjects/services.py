from typing import List

from fastapi import Depends, HTTPException

from checking_code.apps.subjects.managers import SubjectsManager
from checking_code.apps.subjects.schemas import (
    CreateSubjectSchema,
    SubjectReturnData,
    UpdateSubjectFieldsRequest,
)


class SubjectsService:
    def __init__(self, manager: SubjectsManager = Depends(SubjectsManager)) -> None:
        self.manager = manager

    async def create_subject(self, subject: CreateSubjectSchema) -> SubjectReturnData:
        return await self.manager.create_subject(subject=subject)

    async def get_subject(self, id: int) -> SubjectReturnData:
        return await self.manager.get_subject(id=id)

    async def get_subjects(self) -> List[SubjectReturnData]:
        return await self.manager.get_subjects()

    async def update_subject_fields(
        self, id: int, data: UpdateSubjectFieldsRequest
    ) -> SubjectReturnData:
        payload = data.model_dump(exclude_unset=True)
        payload.pop("id", None)
        if not (payload):
            raise HTTPException(status_code=400, detail="No fields to update")
        return await self.manager.update_subject_fields(id=id, **payload)

    async def delete_subject(self, id: int) -> SubjectReturnData:
        return await self.manager.delete_subject(id=id)
