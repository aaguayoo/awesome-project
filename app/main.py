"""Awesome Python Project - API main app."""

from fastapi import FastAPI  # type: ignore

from app.api.v1.routers import awesome_project as v1_awesome_project
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
)

# Registrar routers para cada versión
app.include_router(
    v1_awesome_project.router, 
    prefix="/v1/awesome_project", 
    tags=["Awesome Python Project v1"],
)


@app.get("/")
def read_root() -> dict:
    """Read root."""
    return {"message": "API with versioning is running"}
