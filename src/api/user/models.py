from datetime import datetime
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so

from src.database import Base
from src.api.user.schemas import User


class User(Base):   # noqa
    __tablename__ = "user"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(nullable=False)
    surname: so.Mapped[Optional[str]] = so.mapped_column(nullable=True)
    create_date: so.Mapped[datetime] = so.mapped_column(nullable=False, default=datetime.utcnow)
    password_hash: so.Mapped[str] = so.mapped_column(nullable=False)
    stat_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("statistic.id"), nullable=True)

    def to_read_model(self) -> User:
        return User(
            id=self.id,
            name=self.name,
            surname=self.surname,
            create_date=self.create_date,
            stat_id=self.stat_id
        )

