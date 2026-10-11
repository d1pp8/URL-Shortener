

from fastapi import APIRouter, Depends, Path, Body, status, HTTPException
from fastapi.responses import RedirectResponse
from typing import Annotated

from app.exceptins import NotLongUrlFoundError
from app.services.url_services import generate_url, get_url_by_slug



router = APIRouter()

@router.post("/short_url")
async def generate_short_url(long_url: Annotated[str, Body(embed=True)]):
    new_slug = await generate_url(long_url)
    return new_slug

@router.get("/{slug}")
async def redirect_to_url(slug: Annotated[str, Path()]):
    try:
        long_url = await get_url_by_slug(slug)
    except NotLongUrlFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Link not found")
    return RedirectResponse(url=long_url, status_code=status.HTTP_302_FOUND)