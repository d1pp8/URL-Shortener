from db.connections import async_session
from db.models import ShortURL




async def add_slug_to_database(slug: str, long_url: str):
    async with async_session() as session:
        new_slug = ShortURL(slug=slug, long_url=long_url)
        session.add(new_slug)
        await session.commit()
