from typing import Optional
import datetime

from pydantic import BaseModel, Field


class CreateLessonSchema(BaseModel):
    lesson_datetime: datetime.datetime
    assignment_description: str
    attachment_path: str
    assignment_deadline: datetime.datetime
    group_id: int
    subject_id: int


class LessonReturnData(CreateLessonSchema):
    id: int


class UpdateLessonFieldRequests(BaseModel):
    lesson_datetime: Optional[datetime.datetime]
    assignment_description: Optional[str]
    attachment_path: Optional[str]
    assignment_deadline: Optional[datetime.datetime]
    group_id: Optional[int]
    subject_id: Optional[int]
