from db.connections import async_session
from db.models import ShortURL



async def add_slug_to_database(slug: str, long_url: str) -> None:
    async with async_session() as session:
        new_slug = ShortURL(slug=slug, long_url=long_url)
        session.add(new_slug)
        await session.commit()



async def get_url(slug: str) -> str | None:
    async with async_session() as session:
        query = select(ShortURL).filter_by(slug=slug)
        result = await session.execute(query)
        res = result.scalar_one_or_none()
        return res.long_url if res.long_url else None