"""
Vessel Specifications API
A simple REST API built with FastAPI to manage ship/vessel technical specifications.

Run locally with:
    uvicorn main:app --reload

Then open http://127.0.0.1:8000/docs for interactive Swagger documentation.
"""

from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Vessel Specifications API",
    description="A REST API to create, read, update, and delete ship/vessel technical specifications.",
    version="1.0.0",
)

# ---------------------------------------------------------------------------
# Data models (Pydantic handles request validation + response serialization)
# ---------------------------------------------------------------------------

class VesselBase(BaseModel):
    name: str = Field(..., example="Ever Given")
    imo_number: str = Field(
        ..., min_length=7, max_length=7,
        description="7-digit IMO ship identification number",
        example="9811000",
    )
    vessel_type: str = Field(..., example="Container Ship")
    flag_state: str = Field(..., example="Panama")
    length_overall_m: float = Field(..., gt=0, description="Length overall in meters", example=399.94)
    beam_m: float = Field(..., gt=0, description="Beam (width) in meters", example=58.8)
    draft_m: float = Field(..., gt=0, description="Draft in meters", example=14.5)
    gross_tonnage: int = Field(..., gt=0, example=219079)
    year_built: int = Field(..., ge=1900, le=2100, example=2018)


class VesselCreate(VesselBase):
    """Fields required when creating a vessel (no id yet)."""
    pass


class Vessel(VesselBase):
    """Full vessel record, including the server-assigned id."""
    id: int


# ---------------------------------------------------------------------------
# In-memory "database"
# For a basic/learning project this keeps things simple and dependency-free.
# In a production system this list would be replaced by a real database
# (e.g. PostgreSQL via SQLAlchemy) — the endpoint logic below would barely change.
# ---------------------------------------------------------------------------

vessels_db: List[Vessel] = []
_next_id = 1


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/", tags=["Root"])
def root():
    return {"message": "Vessel Specifications API is running. Visit /docs for interactive documentation."}


@app.post("/vessels", response_model=Vessel, status_code=status.HTTP_201_CREATED, tags=["Vessels"])
def create_vessel(vessel: VesselCreate):
    """Create a new vessel record."""
    global _next_id
    new_vessel = Vessel(id=_next_id, **vessel.dict())
    vessels_db.append(new_vessel)
    _next_id += 1
    return new_vessel


@app.get("/vessels", response_model=List[Vessel], tags=["Vessels"])
def list_vessels(vessel_type: Optional[str] = None):
    """List all vessels. Optionally filter by vessel_type, e.g. /vessels?vessel_type=Tanker"""
    if vessel_type:
        return [v for v in vessels_db if v.vessel_type.lower() == vessel_type.lower()]
    return vessels_db


@app.get("/vessels/{vessel_id}", response_model=Vessel, tags=["Vessels"])
def get_vessel(vessel_id: int):
    """Get a single vessel by its id."""
    for v in vessels_db:
        if v.id == vessel_id:
            return v
    raise HTTPException(status_code=404, detail="Vessel not found")


@app.put("/vessels/{vessel_id}", response_model=Vessel, tags=["Vessels"])
def update_vessel(vessel_id: int, updated: VesselCreate):
    """Replace an existing vessel's specifications."""
    for idx, v in enumerate(vessels_db):
        if v.id == vessel_id:
            new_v = Vessel(id=vessel_id, **updated.dict())
            vessels_db[idx] = new_v
            return new_v
    raise HTTPException(status_code=404, detail="Vessel not found")


@app.delete("/vessels/{vessel_id}", status_code=status.HTTP_200_OK, tags=["Vessels"])
def delete_vessel(vessel_id: int):
    """Delete a vessel by its id."""
    for idx, v in enumerate(vessels_db):
        if v.id == vessel_id:
            vessels_db.pop(idx)
            return {"message": f"Vessel {vessel_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Vessel not found")
