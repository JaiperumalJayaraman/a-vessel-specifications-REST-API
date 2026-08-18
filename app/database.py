from typing import List

from .models import Vessel


vessels_db: List[Vessel] = []
_next_id = 1


def create_vessel(vessel_data: dict) -> Vessel:
    global _next_id
    vessel = Vessel(id=_next_id, **vessel_data)
    vessels_db.append(vessel)
    _next_id += 1
    return vessel


def get_vessels(vessel_type: str | None = None) -> List[Vessel]:
    if vessel_type:
        return [
            vessel
            for vessel in vessels_db
            if vessel.vessel_type.lower() == vessel_type.lower()
        ]
    return vessels_db


def get_vessel(vessel_id: int) -> Vessel | None:
    return next((vessel for vessel in vessels_db if vessel.id == vessel_id), None)


def update_vessel(vessel_id: int, vessel_data: dict) -> Vessel | None:
    for index, vessel in enumerate(vessels_db):
        if vessel.id == vessel_id:
            updated_vessel = Vessel(id=vessel_id, **vessel_data)
            vessels_db[index] = updated_vessel
            return updated_vessel
    return None


def delete_vessel(vessel_id: int) -> bool:
    for index, vessel in enumerate(vessels_db):
        if vessel.id == vessel_id:
            vessels_db.pop(index)
            return True
    return False
