from fastapi import FastAPI
from app.api.shortener import router as shortener_router


app = FastAPI()

app.include_router(shortener_router, prefix='/api/v1', tags=['shortener'])