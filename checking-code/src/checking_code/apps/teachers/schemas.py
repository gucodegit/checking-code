from typing import Optional

from pydantic import BaseModel, Field


class CreateTeacherSchema(BaseModel):
    fullname: str = Field(max_length=100)


class TeacherReturnData(CreateTeacherSchema):
    id: int


class UpdateTeacherFieldRequest(BaseModel):
    fullname: Optional[str] = Field(default=None, max_length=100)
