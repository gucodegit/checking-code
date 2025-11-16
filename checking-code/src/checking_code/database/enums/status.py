from enum import Enum


class AssignmentStatus(str, Enum):
    SUBMITTED = "submitted"
    AUTO_CHECKED = "auto_checked"
    TEACHER_CHECKED = "teacher_checked"
