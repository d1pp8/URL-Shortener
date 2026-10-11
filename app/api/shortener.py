from fastapi import APIRouter, Depends, Path, Body
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from app.services.url_services import generate_url



router = APIRouter()

@router.post("/short_url")
async def generate_short_url(long_url: Annotated[str, Body(embed=True)]):
    new_slug = await generate_url(long_url)
    return new_slug

@router.get("/{slug}")
async def redirect_to_url(slug: Annotated[str, Path()]):
    return slug