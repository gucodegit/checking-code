from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from checking_code.database.models import Base
from checking_code.database.mixins.id_mixins import IDMixin


class Students(IDMixin, Base):
    fullname: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )
    group_id: Mapped[int] = mapped_column(
        ForeignKey("groups.id", ondelete="CASCADE"),
    )
