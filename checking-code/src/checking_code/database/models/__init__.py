from checking_code.database.models.base import Base
from checking_code.database.models.student import Students
from checking_code.database.models.teacher import Teachers
from checking_code.database.models.group import Groups
from checking_code.database.models.subject import Subjects
from checking_code.database.models.lesson import Lessons
from checking_code.database.models.assignment import Assignments


__all__ = (
    "Base",
    "Teachers",
    "Groups",
    "Subjects",
    "Lessons",
    "Assignments",
)
