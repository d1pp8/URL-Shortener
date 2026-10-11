from fastapi import APIRouter, Depends, Path, Body
from sqlalchemy.ext.asyncio import AsyncSession

from contextlib import asynccontextmanager
from typing import Annotated




router = APIRouter()


@router.post("/short_url")
async def generate_short_url(long_url: Annotated[str, Body(embed=True)]):
    return ...


@router.get("/{slug}")
async def redirect_to_url(slug: Annotated[str, Path()]):
    return slug