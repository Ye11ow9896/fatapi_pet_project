from datetime import datetime

import sqlalchemy.orm as so

from src.database import Base


class Statistic(Base):
    __tablename__ = "statistic"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    date: so.Mapped[datetime] = so.mapped_column(nullable=False, default=datetime.utcnow)
    request: so.Mapped[str] = so.mapped_column(nullable=False)
    result: so.Mapped[int] = so.mapped_column(nullable=False, default=None)
