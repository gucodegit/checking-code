import datetime

from sqlalchemy import String, Text, JSON, Numeric, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from checking_code.database.models.base import Base
from checking_code.database.mixins.id_mixins import IDMixin
from checking_code.database.enums.status import AssignmentStatus


class Assignments(IDMixin, Base):
    lesson_id: Mapped[int] = mapped_column(
        ForeignKey("lessons.id", ondelete="CASCADE"),
    )
    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id", ondelete="CASCADE"),
    )
    submission_text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    submission_file_path: Mapped[str] = mapped_column(
        Text,
        unique=True,
        nullable=False,
    )
    submission_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    # op.execute("DROP TYPE assignment_status_enum")
    status: Mapped[AssignmentStatus] = mapped_column(
        Enum(AssignmentStatus, name="assignment_status_enum"),
        default=AssignmentStatus.SUBMITTED,
        nullable=False,
    )
    auto_check_result: Mapped[dict] = mapped_column(
        JSON,
        nullable=True,
    )
    teacher_feedback: Mapped[str] = mapped_column(
        Text,
        nullable=True,
    )
    teacher_score: Mapped[float] = mapped_column(
        Numeric(5, 2),
        nullable=True,
    )
    checked_by: Mapped[int] = mapped_column(
        ForeignKey("teachers.id", ondelete="CASCADE"),
        nullable=True,
    )
    checked_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    max_score: Mapped[int] = mapped_column(
        Integer,
        nullable=True,
    )
