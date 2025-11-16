from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from checking_code.database.models import Base
from checking_code.database.mixins.id_mixins import IDMixin


class Subjects(IDMixin, Base):
    subject_name: Mapped[str] = mapped_column(
        String(100),
        unique=False,
        nullable=False,
    )
    teacher_id: Mapped[int] = mapped_column(
        ForeignKey("teachers.id", ondelete="CASCADE"),
    )
