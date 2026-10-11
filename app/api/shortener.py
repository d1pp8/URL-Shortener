from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from typing import Annotated




router = APIRouter()


@router.post("/generate_url")
async def generate_short_url():
    return ...


@router.get("/{slug}")
async def redirect_to_url(slug: Annotated[str, Path()]):
    return slug