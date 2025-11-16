from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from checking_code.database.models import Base
from checking_code.database.mixins.id_mixins import IDMixin


class Groups(IDMixin, Base):
    group_name: Mapped[str] = mapped_column(
        String(10),
        unique=True,
        nullable=False,
    )
