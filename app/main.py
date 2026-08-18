from fastapi import FastAPI

from .routes import router as vessel_router

app = FastAPI(
    title="Vessel Specifications API",
    description="REST API for managing technical specifications of vessels.",
    version="1.0.0",
)

app.include_router(vessel_router)
