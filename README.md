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

## Data Storage
This version stores data **in memory** (a Python list) so it has zero external
dependencies and resets each time the server restarts. That keeps the project
simple to run and explain. A natural next step would be swapping in a real
database (e.g. SQLite/PostgreSQL via SQLAlchemy) — the route logic wouldn't
need to change, just the storage layer underneath it.

## Possible Extensions
- Persistent storage (SQLite/PostgreSQL)
- Pagination on `GET /vessels`
- Authentication (API key or JWT)
- Automated tests with `pytest` + `TestClient`

---

## How to Explain This in an Interview

**"What is this project?"**
A REST API for managing vessel specifications — standard CRUD operations
(Create, Read, Update, Delete) over HTTP.

**"Why FastAPI?"**
It's a modern Python web framework that's fast to build with, gives you
automatic request validation, and generates interactive API docs (Swagger)
for free — good for both development speed and documentation.

**"How does validation work?"**
Each request body is validated against a Pydantic model. If a field is
missing, the wrong type, or fails a constraint (e.g. `gross_tonnage` must be
greater than 0), FastAPI automatically returns a `422 Unprocessable Entity`
with details — no manual validation code needed.

**"Why those HTTP methods and status codes?"**
- `POST` → create → `201 Created`
- `GET` → read → `200 OK`
- `PUT` → full update → `200 OK`
- `DELETE` → remove → `200 OK`
- Requesting a vessel that doesn't exist → `404 Not Found`

This follows REST convention: the URL identifies the *resource*
(`/vessels/{id}`), and the HTTP method identifies the *action* on it.

**"What's the current limitation?"**
Data lives in memory, so it's lost on restart — fine for a demo, not for
production. The fix is a real database, and because the route functions
only talk to a `vessels_db` variable, that swap is isolated to one layer.
