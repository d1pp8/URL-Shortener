import string
from secrets import choice
from app.repository.shortener import add_slug_to_database


ALPHABET: str = string.ascii_letters + string.digits

def generate_random_slug() -> str:
    slug = ""
    for _ in range(6):
        slug += choice(ALPHABET)
    return slug



async def generate_url(long_url):
    slug = generate_random_slug()
    await add_slug_to_database(slug=slug, long_url=long_url)

    return slug

