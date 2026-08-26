from fastapi import FastAPI
import quiz
from pydantic import BaseModel

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/questions")
def get_questions():
    data = quiz.load_questions_json()
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
    result = quiz.build_result(
        name = payload.name,
        score = payload.score,
        total_questions = payload.total_questions,
        selected_difficulty = payload.selected_difficulty,
        wrong_catagories = payload.wrong_catagories,
        wrong_difficulties = payload.wrong_difficulties,
        
    )
    quiz.save_result_json(result)
    return result

@app.get("/results")
def get_results():
    data = quiz.load_results_json()
    return data