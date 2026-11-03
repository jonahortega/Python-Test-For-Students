# Programming Quiz (Python for Beginners)

A Python Quiz built for begginers to test their knowledge of the Python programming Language. This was built to practice real world applications of professional software engineering and standards.



## Features
- Multi-file CLI (main, menu, quiz, review)
- JSON question bank and result history
- FastAPi layer for API endppints, 5 endpoints in total (GET /health, GET /questions, POST /results, GET /results, GET /results/{name})
- Pytest tests for:
    - test_quiz.py:  `build_result`, `build_result_score`
    - test_api.py: `test_health`, `test_questions_hide_answers`, `test_create_result_success`, `test_create_result_zero_questions`, `test_get_result_by_name`

## Setup
1. Clone the repo
2. Create venv: `python3 -m venv .venv`
3. Activate: `source .venv/bin/activate`
4. Install: `pip install -r requirements.txt`
5. Run: `python main.py`
6. Test: `pytest -v`

## Project structure
- `main.py` — entry point
- `menu.py` — menu loop
- `quiz.py` — quiz logic + JSON
- `tests/` — pytest

## Roadmap
- [X] FastAPI layer
- [ ] SQLAlchemy + PostgreSQL
- [ ] Dockerize the project
- [ ] Add a frontend to the project
