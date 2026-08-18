# Vessel Specifications REST API

A simple REST API built with **Python and FastAPI** for managing technical specifications of vessels.

This project demonstrates core backend concepts: RESTful endpoints, CRUD operations, request validation, filtering, error handling, and automated API testing.

## Tech Stack

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- HTTPX

## Project Structure

```text
vessel-specifications-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── routes.py
├── tests/
│   └── test_vessels.py
├── requirements.txt
└── README.md
```

## Run Locally

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` to use the interactive API documentation.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/vessels` | Create a vessel |
| GET | `/vessels` | List vessels |
| GET | `/vessels/{id}` | Get a vessel by ID |
| PUT | `/vessels/{id}` | Update a vessel |
| DELETE | `/vessels/{id}` | Delete a vessel |

### Filtering

Vessels can be filtered by type:

```text
GET /vessels?vessel_type=Container%20Ship
```

## Example Request

```json
{
  "name": "Ever Given",
  "imo_number": "9811000",
  "vessel_type": "Container Ship",
  "flag_state": "Panama",
  "length_overall_m": 399.94,
  "beam_m": 58.8,
  "draft_m": 14.5,
  "gross_tonnage": 219079,
  "year_built": 2018
}
```

## Validation

Pydantic validates incoming vessel data, including positive vessel dimensions and tonnage, a 7-character IMO number, and a valid construction year range.

## Testing

Run the automated tests with:

```bash
pytest
```

The current project uses an in-memory data store to keep the implementation focused on REST API fundamentals. Data is reset when the application restarts.
