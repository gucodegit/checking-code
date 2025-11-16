import datetime

from sqlalchemy import Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from checking_code.database.models import Base
from checking_code.database.mixins.id_mixins import IDMixin


class Lessons(IDMixin, Base):
    lesson_datetime: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    assignment_description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    attachment_path: Mapped[str] = mapped_column(
        Text,
        unique=True,
        nullable=False,
    )
    assignment_deadline: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    group_id: Mapped[int] = mapped_column(
        ForeignKey("groups.id", ondelete="CASCADE"),
    )
    subject_id: Mapped[int] = mapped_column(
        ForeignKey("subjects.id", ondelete="CASCADE"),
    )
