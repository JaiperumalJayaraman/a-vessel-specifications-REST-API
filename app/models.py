from pydantic import BaseModel, Field


class VesselBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    imo_number: str = Field(..., min_length=7, max_length=7)
    vessel_type: str = Field(..., min_length=1, max_length=50)
    flag_state: str = Field(..., min_length=1, max_length=50)
    length_overall_m: float = Field(..., gt=0)
    beam_m: float = Field(..., gt=0)
    draft_m: float = Field(..., gt=0)
    gross_tonnage: int = Field(..., gt=0)
    year_built: int = Field(..., ge=1900, le=2100)


class VesselCreate(VesselBase):
    pass


class Vessel(VesselBase):
    id: int
