# Programming Quiz API (v0)

Backend quiz project with a multi-file CLI, a FastAPI HTTP layer, and PostgreSQL persistence through SQLAlchemy. Built to practice professional software engineering standards and practices. 

**Status:** v0 is working locally (API + Postgres + tests). v1 plans are listed below.

## What it does

Players take a Python quiz by difficulty/category. Results can be recorded two ways:

- CLI (`python main.py`) — stores history in JSON files
- HTTP API (`app/main.py`) — stores results in PostgreSQL

`GET /questions` returns questions without answers so clients can show prompts without getting the answer key.

## Stack

- Python 3
- FastAPI + Uvicorn
- SQLAlchemy + PostgreSQL (psycopg2)
- pytest (quiz logic + API tests)
- CLI modules: `main.py`, `menu.py`, `quiz.py`, `review.py`

## API endpoints (v0)

| Method | Path | What it does |
|--------|------|--------------|
| GET | `/health` | Health check |
| GET | `/questions` | Questions for clients (no answers) |
| POST | `/results` | Validate input, build result, save to Postgres |
| GET | `/results` | List all results |
| GET | `/results/{name}` | Results filtered by name |

Docs when the server is running: http://127.0.0.1:8000/docs

## Features

- Multi-file CLI quiz
- JSON question bank
- FastAPI layer with the endpoints above
- SQLAlchemy + PostgreSQL for API result storage
- pytest coverage for core quiz logic and API behavior (health, answer hiding, create, validation, get-by-name)

## Setup

1. Clone the repo
2. Create a virtualenv: `python3 -m venv .venv`
3. Activate: `source .venv/bin/activate`
4. Install deps: `pip install -r requirements.txt`
5. Start PostgreSQL locally and create a database
6. Refer to the .env.example file to set the DATABASE_URL environment variable
7. Start the API: `uvicorn app.main:app --reload`
8. Open docs: http://127.0.0.1:8000/docs
9. Optional CLI: `python main.py`
10. Run tests: `pytest -v`

Note: API tests use the same database URL, so pytest can insert sample rows into your local `results` table.

## Project structure

- `app/main.py` — FastAPI routes
- `app/database.py` — SQLAlchemy engine, Result model, save/load
- `quiz.py` — shared quiz logic
- `main.py`, `menu.py`, `review.py` — CLI
- `questions.json` — question bank
- `tests/` — pytest (`test_api.py`, `test_quiz.py`)

## v0 (done)

- [x] Multi-file CLI
- [x] FastAPI endpoints
- [x] SQLAlchemy + PostgreSQL for API results
- [x] pytest for quiz logic and API behavior

## v1 (planned)

- [X] Move database URL to an environment variable
- [ ] Docker Compose (app + Postgres)
- [ ] Point CLI at the same DB (or call the API)
- [ ] Isolate tests from the personal/dev database
- [ ] Add a frontend against the API
- [ ] Auth / tighter access to results

## Design notes

- `POST /results` rejects `total_questions == 0` with HTTP 400
- `GET /questions` hides answers on purpose
- API uses `quiz.build_result` so result shape stays consistent
- Connection string is now int he environment variable; env + Docker are v1 work