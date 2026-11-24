from fastapi import FastAPI, HTTPException
import quiz
from pydantic import BaseModel
from app.database import save_result_db, load_results_db

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/questions")
def get_questions():
    data = quiz.load_questions_for_client()
    return data

class ResultCreate(BaseModel):
    name : str
    score: int
    total_questions : int
    selected_difficulty : str
    wrong_catagories: dict = {}
    wrong_difficulties : dict = {}
    
@app.post("/results")
def create_result(payload: ResultCreate):
    if payload.total_questions == 0:
        raise HTTPException(
            status_code=400,
            detail="total_questions must be greater than 0",
        )
    result = quiz.build_result(
        name = payload.name,
        score = payload.score,
        total_questions = payload.total_questions,
        selected_difficulty = payload.selected_difficulty,
        wrong_catagories = payload.wrong_catagories,
        wrong_difficulties = payload.wrong_difficulties,
        
    )
    save_result_db(result)
    return result

@app.get("/results")
def get_results():
    data = load_results_db()
    return data

@app.get("/results/{name}")
def get_result_by_name(name:str):
    all_results = load_results_db()
    data = quiz.filter_results_by_name(all_results,name)
    return data