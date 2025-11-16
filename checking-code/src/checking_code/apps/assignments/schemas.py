from typing import Optional
import datetime

from pydantic import BaseModel, Field

from checking_code.database.enums.status import AssignmentStatus


class CreateAssignmentSchema(BaseModel):
    lesson_id: int
    student_id: int
    submission_text: str
    submission_file_path: str
    submission_date: datetime.datetime
    status: AssignmentStatus = Field(default=AssignmentStatus.SUBMITTED)
    auto_check_result: Optional[dict] = Field(default=None)
    teacher_feedback: Optional[str] = Field(default=None)
    teacher_score: Optional[float] = Field(default=None)
    checked_by: Optional[int] = Field(default=None)
    checked_date: Optional[datetime.datetime] = Field(default=None)
    max_score: Optional[int] = Field(default=None)


class AssignmentReturnData(CreateAssignmentSchema):
    id: int


class UpdateAssignmentFieldsRequest(BaseModel):
    lesson_id: Optional[int]
    student_id: Optional[int]
    submission_text: Optional[str]
    submission_file_path: Optional[str]
    submission_date: Optional[datetime.datetime]
    status: Optional[AssignmentStatus]
    auto_check_result: Optional[dict] = Field(default=None)
    teacher_feedback: Optional[str] = Field(default=None)
    teacher_score: Optional[float] = Field(default=None)
    checked_by: Optional[int] = Field(default=None)
    checked_date: Optional[datetime.datetime] = Field(default=None)
    max_score: Optional[int] = Field(default=None)
