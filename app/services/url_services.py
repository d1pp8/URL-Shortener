import string
from secrets import choice

from app.exceptins import NotLongUrlFoundError
from app.repository.shortener import add_slug_to_database, get_url


ALPHABET: str = string.ascii_letters + string.digits

def _generate_random_slug() -> str:
    slug = ""
    for _ in range(6):
        slug += choice(ALPHABET)
    return slug



async def generate_url(long_url):
    slug = _generate_random_slug()
    await add_slug_to_database(slug=slug, long_url=long_url)

    return slug


async def get_url_by_slug(slug:str) -> str:
    long_url = await get_url(slug)
    if not long_url:
        raise NotLongUrlFoundError()
    return long_url
