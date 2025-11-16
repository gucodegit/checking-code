from typing import Optional

from pydantic import BaseModel, Field


class CreateStudentSchema(BaseModel):
    fullname: str = Field(max_length=100)
    group_id: int


class StudentReturnData(CreateStudentSchema):
    id: int


class UpdateStudentFieldsRequest(BaseModel):
    fullname: Optional[str] = Field(default=None, max_length=100)
    group_id: Optional[int] = None
