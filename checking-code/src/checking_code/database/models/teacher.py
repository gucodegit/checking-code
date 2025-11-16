from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from checking_code.database.models import Base
from checking_code.database.mixins.id_mixins import IDMixin


class Teachers(IDMixin, Base):
    fullname: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )
