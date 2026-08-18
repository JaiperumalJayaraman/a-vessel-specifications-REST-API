from fastapi import APIRouter, HTTPException, status

from .database import create_vessel, delete_vessel, get_vessel, get_vessels, update_vessel
from .models import Vessel, VesselCreate

router = APIRouter(prefix="/vessels", tags=["Vessels"])


@router.post("", response_model=Vessel, status_code=status.HTTP_201_CREATED)
def add_vessel(vessel: VesselCreate):
    return create_vessel(vessel.model_dump())


@router.get("", response_model=list[Vessel])
def list_all_vessels(vessel_type: str | None = None):
    return get_vessels(vessel_type)


@router.get("/{vessel_id}", response_model=Vessel)
def get_single_vessel(vessel_id: int):
    vessel = get_vessel(vessel_id)
    if vessel is None:
        raise HTTPException(status_code=404, detail="Vessel not found")
    return vessel


@router.put("/{vessel_id}", response_model=Vessel)
def replace_vessel(vessel_id: int, vessel: VesselCreate):
    updated_vessel = update_vessel(vessel_id, vessel.model_dump())
    if updated_vessel is None:
        raise HTTPException(status_code=404, detail="Vessel not found")
    return updated_vessel


@router.delete("/{vessel_id}")
def remove_vessel(vessel_id: int):
    if not delete_vessel(vessel_id):
        raise HTTPException(status_code=404, detail="Vessel not found")
    return {"message": f"Vessel {vessel_id} deleted successfully"}
