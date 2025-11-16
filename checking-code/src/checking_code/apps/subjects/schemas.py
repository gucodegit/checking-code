from typing import Optional

from pydantic import BaseModel, Field


class CreateSubjectSchema(BaseModel):
    subject_name: str = Field(max_length=100)
    teacher_id: int


class SubjectReturnData(CreateSubjectSchema):
    id: int


class UpdateSubjectFieldsRequest(BaseModel):
    subject_name: Optional[str] = Field(default=None, max_length=100)
    teacher_id: Optional[int] = None
