import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.controller import router
from app.config import settings


logging.basicConfig(level=logging.INFO)


app = FastAPI(
    title="LinkForge",
    description="A URL shortener service.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allow_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
