from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from db.config import settings


engine = create_async_engine(url=settings.DATA_BASE_URL_ASYNCPG, echo=True)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass