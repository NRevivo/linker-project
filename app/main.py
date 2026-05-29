"""FastAPI application entry point for LinkForge."""

from fastapi import FastAPI

from app.api.controller import router


def create_app() -> FastAPI:
    """Build and configure the FastAPI application instance."""
    ...


app = FastAPI()
app.include_router(router)
