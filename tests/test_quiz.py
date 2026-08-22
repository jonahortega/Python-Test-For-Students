from quiz import build_result

def test_build_result():
    result = build_result(
        name= "Jonah",
        score = 3,
        total_questions = 5,
        selected_difficulty = "all",
        wrong_catagories = {},
        wrong_difficulties={}
    )
    
    assert result["name"] == "Jonah"
    assert result["score"] == 3

def test_build_result_score():
    result = build_result(
        name = "Jonah",
        score = 2,
        total_questions = 2,
        selected_difficulty = "medium",
        wrong_catagories ={},
        wrong_difficulties={},
    )
    assert result["score"] == 2
    assert result["percentage"] == 100
    
def test_build_result_percentage_three_out_of_five():
    result = build_result(
        name = "Jonah",
        score = 3,
        total_questions = 5,
        selected_difficulty = "all",
        wrong_catagories = {
            "lists" : 1,
            "functions" : 1
        },
        wrong_difficulties = {
            "medium": 2
        }
    )
    
    
    assert result["percentage"] == 60