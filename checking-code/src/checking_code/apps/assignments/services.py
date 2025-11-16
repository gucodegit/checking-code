from typing import List

from fastapi import Depends, HTTPException

from checking_code.apps.assignments.managers import AssignmentsManager
from checking_code.apps.assignments.schemas import (
    CreateAssignmentSchema,
    AssignmentReturnData,
    UpdateAssignmentFieldsRequest,
)


class assignmentsService:
    def __init__(
        self, manager: AssignmentsManager = Depends(AssignmentsManager)
    ) -> None:
        self.manager = manager

    async def create_assignment(
        self, assignment: CreateAssignmentSchema
    ) -> AssignmentReturnData:
        return await self.manager.create_assignment(assignment=assignment)

    async def get_assignment(self, id: int) -> AssignmentReturnData:
        return await self.manager.get_assignment(id=id)

    async def get_assignments(self) -> List[AssignmentReturnData]:
        return await self.manager.get_assignments()

    async def update_assignment_fields(
        self, id: int, data: UpdateAssignmentFieldsRequest
    ) -> AssignmentReturnData:
        payload = data.model_dump(exclude_unset=True)
        payload.pop("id", None)
        if not (payload):
            raise HTTPException(status_code=400, detail="No fields to update")
        return await self.manager.update_assignment_fields(id=id, **payload)

    async def delete_assignment(self, id: int) -> AssignmentReturnData:
        return await self.manager.delete_assignment(id=id)
