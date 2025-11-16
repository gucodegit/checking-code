from typing import Optional

from pydantic import BaseModel, Field


class CreateGroupSchema(BaseModel):
    group_name: str = Field(max_length=10)


class GroupReturnData(CreateGroupSchema):
    id: int


class UpdateGroupFieldsRequest(BaseModel):
    group_name: Optional[str] = Field(default=None, max_length=10)
