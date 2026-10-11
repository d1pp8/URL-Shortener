import string
from secrets import choice

from app.exception import NotLongUrlFoundError, SlugAlreadyExistsError
from app.repository.shortener import add_slug_to_database, get_url


ALPHABET: str = string.ascii_letters + string.digits

def _generate_random_slug() -> str:
    slug = ""
    for _ in range(6):
        slug += choice(ALPHABET)
    return slug


async def generate_url(long_url: str) -> str:
    async def _generate_slug_and_add_to_db():
        slug = _generate_random_slug()
        await add_slug_to_database(slug=slug, long_url=long_url)
        return slug
    for attempt in range(5):
        try:
            slug = await _generate_slug_and_add_to_db()
            return slug
        except SlugAlreadyExistsError as ex:
            if attempt == 4:
                raise SlugAlreadyExistsError from ex
    return slug



async def get_url_by_slug(slug:str) -> str:
    long_url = await get_url(slug)
    if not long_url:
        raise NotLongUrlFoundError()
    return long_url
