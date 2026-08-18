# Vessel Specifications API

A REST API built with **Python + FastAPI** to create, read, update, and delete
technical specifications for ships/vessels (name, IMO number, type, dimensions,
tonnage, flag state, year built).

Built as a learning/portfolio project to demonstrate REST API design principles:
resource-based routes, proper HTTP methods and status codes, and request/response
validation.

## Tech Stack
- **Python 3.10+**
- **FastAPI** — web framework
- **Pydantic** — data validation and serialization
- **Uvicorn** — ASGI server

## Project Structure
```
vessel-api/
├── main.py            # API routes + data models
├── requirements.txt    # dependencies
└── README.md
```

## Setup & Run

```bash
# 1. Clone the repo
git clone <your-repo-url>
cd vessel-api

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
uvicorn main:app --reload
```

The API is now running at `http://127.0.0.1:8000`.

Open `http://127.0.0.1:8000/docs` for interactive Swagger UI — you can try every
endpoint from the browser with no extra tools.

## Endpoints

| Method | Endpoint             | Description                              |
|--------|-----------------------|-------------------------------------------|
| GET    | `/`                    | Health check / welcome message            |
| POST   | `/vessels`             | Create a new vessel                       |
| GET    | `/vessels`             | List all vessels (optional `?vessel_type=`) |
| GET    | `/vessels/{id}`        | Get a single vessel by id                 |
| PUT    | `/vessels/{id}`        | Update a vessel                           |
| DELETE | `/vessels/{id}`        | Delete a vessel                           |

## Example Request

```bash
curl -X POST http://127.0.0.1:8000/vessels \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Ever Given",
        "imo_number": "9811000",
        "vessel_type": "Container Ship",
        "flag_state": "Panama",
        "length_overall_m": 399.94,
        "beam_m": 58.8,
        "draft_m": 14.5,
        "gross_tonnage": 219079,
        "year_built": 2018
      }'
```

Response:
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
  "year_built": 2018,
  "id": 1
}
```

Data lives in memory, so it's lost on restart — fine for a demo, not for
production. The fix is a real database, and because the route functions
only talk to a `vessels_db` variable, that swap is isolated to one layer.
