# Python Quiz Learning Project

CLI quiz app built to practice real world applications of Python as a professional software engineer. A guided learning project with Lior Abitbol.

## Features
- Multi-file CLI (main, menu, quiz, review)
- JSON question bank and result history
- Pytest tests for `build_result`

## Setup
1. Clone the repo
2. Create venv: `python3 -m venv .venv`
3. Activate: `source .venv/bin/activate`
4. Install: `pip install pytest`
5. Run: `python main.py`
6. Test: `pytest -v`

## Project structure
- `main.py` — entry point
- `menu.py` — menu loop
- `quiz.py` — quiz logic + JSON
- `tests/` — pytest

## Roadmap
- [ ] FastAPI layer
- [ ] SQLAlchemy + PostgreSQL