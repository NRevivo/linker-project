import logging

from fastapi import FastAPI

from app.api.controller import router


logging.basicConfig(level=logging.INFO)


app = FastAPI(
    title="LinkForge",
    description="A URL shortener service.",
    version="0.1.0",
)

app.include_router(router)