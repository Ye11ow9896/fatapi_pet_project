import sqlalchemy.orm as so

from src.database import Base
from src.api.api_source import schemas


class ApiSource(Base):
    """
    Таблица источников API
    """
    __tablename__ = 'apiSource'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(nullable=False)
    type: so.Mapped[str] = so.mapped_column(nullable=False)
    url: so.Mapped[str] = so.mapped_column(nullable=False)
    header_key: so.Mapped[str] = so.mapped_column(nullable=False)

    def read_table(self) -> schemas.ApiSource:
        return ApiSource(
            id=self.id,
            name=self.name,
            type=self.type,
            url=self.url,
            header_key=self.header_key
        )
