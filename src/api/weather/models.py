from datetime import datetime
from typing import Optional, List
import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy import Integer, String

from src.database import Base
from src.api.weather import schemas


class Region(Base):
    __tablename__ = 'region'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(nullable=False)
    lat: so.Mapped[float] = so.mapped_column(nullable=False)
    lon: so.Mapped[float] = so.mapped_column(nullable=False)

    weather: so.Mapped[List["Weather"]] = so.relationship(back_populates="region")

    def read_table(self) -> schemas.Region:
        return schemas.Region(
            id=self.id,
            name=self.name,
            lat=self.lat,
            lon=self.lon
        )

    def read_custom(self) -> schemas.CustomRegion:
        """
        Возвращаем данные, содержащиеся в таблице и с relationship
        """
        return schemas.CustomRegion(
            id=self.id,
            name=self.name,
            lat=self.lat,
            lon=self.lon,
            weather=self.weather
        )


class Weather(Base):
    __tablename__ = 'weather'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    id_region: so.Mapped[int] = so.mapped_column(sa.ForeignKey("region.id"), nullable=True)
    date: so.Mapped[datetime] = so.mapped_column(nullable=False, default=datetime.utcnow)
    temp: so.Mapped[int] = so.mapped_column(nullable=False)
    feel_like: so.Mapped[int] = so.mapped_column(nullable=False)
    condition: so.Mapped[str] = so.mapped_column(nullable=False)
    wind_speed: so.Mapped[int] = so.mapped_column(nullable=False)
    wind_dir: so.Mapped[str] = so.mapped_column(nullable=False)
    pressure_mm: so.Mapped[int] = so.mapped_column(nullable=False)
    pressure_pa: so.Mapped[int] = so.mapped_column(nullable=False)
    humidity: so.Mapped[int] = so.mapped_column(nullable=False)
    sunrise: so.Mapped[str] = so.mapped_column(nullable=False)
    sunset: so.Mapped[str] = so.mapped_column(nullable=False)

    region: so.Mapped["Region"] = so.relationship(back_populates="weather")

    def read_table(self) -> schemas.Weather:
        return schemas.Weather(
            id=self.id,
            id_region=self.id_region,
            date=self.date,
            temp=self.temp,
            feel_like=self.feel_like,
            condition=self.condition,
            wind_speed=self.wind_speed,
            wind_dir=self.wind_dir,
            pressure_mm=self.pressure_mm,
            pressure_pa=self.pressure_pa,
            humidity=self.humidity,
            sunrise=self.sunrise,
            sunset=self.sunset
        )
