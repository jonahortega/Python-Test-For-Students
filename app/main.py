from fastapi import FastAPI
import quiz


app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/questions")
def get_questions():
    data = quiz.load_questions_json()
    return data