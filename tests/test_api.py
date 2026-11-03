from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}
    
def test_questions_hide_answers():
    response = client.get("/questions")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data)>0
    
    first_question = data[0]
    assert "question" in first_question
    assert "answer" not in first_question
    
def test_create_result_success():
    response = client.post("/results", json={
        "name": "Tyler",
        "score": 5,
        "total_questions": 5,
        "selected_difficulty": "all"
    })
    assert response.status_code==200
    assert response.json()["percentage"]==100
    assert response.json()["name"]=="Tyler"
    
def test_create_result_zero_questions():
    response = client.post("/results", json={
        "name": "Tyler",
        "score": 0,
        "total_questions": 0,
        "selected_difficulty": "medium"
    })
    assert response.status_code==400
    
def test_get_result_by_name():
    response = client.post("/results", json={
        "name": "Jonah",
        "score" : 3,
        "total_questions" : 5,
        "selected_difficulty" : "all"
    })
    response = client.get("/results/Jonah")
    
    assert response.status_code==200
    
    data = response.json()
    assert len(data)>0
    
    for item in data:
        assert item["name"]=="Jonah"
    
    