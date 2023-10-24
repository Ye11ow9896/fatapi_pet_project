from datetime import datetime
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so

from src.database import Base
from src.api.user import schemas


class User(Base):   # noqa
    __tablename__ = "user"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(nullable=False)
    surname: so.Mapped[Optional[str]] = so.mapped_column(nullable=True)
    login: so.Mapped[str] = so.mapped_column(nullable=False)
    create_date: so.Mapped[datetime] = so.mapped_column(nullable=False, default=datetime.utcnow)
    password: so.Mapped[str] = so.mapped_column(nullable=False)
    stat_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("statistic.id"), nullable=True)

    def to_read_model(self) -> schemas.User:
        return User(
            id=self.id,
            name=self.name,
            surname=self.surname,
            login=self.login,
            create_date=self.create_date,
            stat_id=self.stat_id
        )

