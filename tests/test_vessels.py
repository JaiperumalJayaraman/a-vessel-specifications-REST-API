from fastapi.testclient import TestClient

from app.main import app
from app.database import vessels_db

client = TestClient(app)


def setup_function():
    vessels_db.clear()


def sample_vessel():
    return {
        "name": "Ever Given",
        "imo_number": "9811000",
        "vessel_type": "Container Ship",
        "flag_state": "Panama",
        "length_overall_m": 399.94,
        "beam_m": 58.8,
        "draft_m": 14.5,
        "gross_tonnage": 219079,
        "year_built": 2018,
    }


def test_create_vessel():
    response = client.post("/vessels", json=sample_vessel())
    assert response.status_code == 201
    assert response.json()["name"] == "Ever Given"


def test_get_vessel():
    create_response = client.post("/vessels", json=sample_vessel())
    vessel_id = create_response.json()["id"]

    response = client.get(f"/vessels/{vessel_id}")
    assert response.status_code == 200
    assert response.json()["id"] == vessel_id


def test_get_missing_vessel():
    response = client.get("/vessels/999")
    assert response.status_code == 404


def test_delete_vessel():
    create_response = client.post("/vessels", json=sample_vessel())
    vessel_id = create_response.json()["id"]

    response = client.delete(f"/vessels/{vessel_id}")
    assert response.status_code == 200
    assert client.get(f"/vessels/{vessel_id}").status_code == 404
