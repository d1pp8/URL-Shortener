from db.connections import Base
from sqlalchemy import MetaData
from sqlalchemy.orm import Mapped, mapped_column


class ShortURL(Base):
    __tablename__ = "short_urls"

    slug: Mapped[str] = mapped_column(primary_key=True)
    long_url: Mapped[str] = mapped_column()