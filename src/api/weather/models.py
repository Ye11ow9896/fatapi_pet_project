from datetime import datetime
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so

from src.database import Base
from src.api.weather import schemas


#class Weather(Base):   # noqa
#    __tablename__ = "weather"
#
#    id: so.Mapped[int] = so.mapped_column(primary_key=True)
#    id_user: so.Mapped[str] = so.mapped_column(sa.ForeignKey("user.id"), nullable=True)
#    create_date: so.Mapped[datetime] = so.mapped_column(nullable=False, default=datetime.utcnow)
#
#
#    def to_read_model(self) -> User:
#        return User(
#            id=self.id,
#            name=self.name,
#            surname=self.surname,
#            login=self.login,
#            create_date=self.create_date,
#            stat_id=self.stat_id
#        )

class Region(Base):
    __tablename__ = 'region'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(nullable=False)
    lat: so.Mapped[float] = so.mapped_column(nullable=False)
    lon: so.Mapped[float] = so.mapped_column(nullable=False)

    def to_read_model(self) -> schemas.Region:
        return Region(
            id=self.id,
            name=self.name,
            lat=self.lat,
            lon=self.lon
        )
