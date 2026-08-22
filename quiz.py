import json
from datetime import datetime


def ask_question(question_text, correct_answer):

    answer = input(question_text).lower().strip()
        
    if answer == correct_answer.lower().strip():
        print("Correct!")
        return True
    
    else:
        print(f"Incorrect, the answer is {correct_answer}")
        
        return False
    
def choose_difficulty():
    thedifficulty = input("Choose a difficulty: \n 1. Easy \n 2. Medium \n 3. Hard \n 4. All \n")
    
    if thedifficulty == "1":
        return "easy"
    elif thedifficulty == "2":
        return "medium"
    elif thedifficulty == "3":
        return "hard"
    elif thedifficulty == "4":
        return "all"
    else:
        print("Invalid difficulty")
        return None 
    
def build_result(name, score, total_questions, selected_difficulty, wrong_catagories, wrong_difficulties):
    percentage = (score / total_questions) * 100
    date_taken = datetime.now().strftime("%Y-%m-%d %H:%M")
    return {
        "name": name,
        "score": score,
        "total_questions": total_questions,
        "selected_difficulty": selected_difficulty,
        "wrong_catagories": wrong_catagories,
        "wrong_difficulties": wrong_difficulties,
        "percentage": percentage,
        "date_taken": date_taken,
    }
    
def save_result_json(result):
    try:
        with open("results.json", "r") as file:
            results = json.load(file)
    except FileNotFoundError:
        results = []
        
    results.append(result)
    with open("results.json", "w") as file:
            json.dump(results,file, indent=4)

def save_wrong_questions(wrong_questions):
    # Simpler than results: just overwrite the file with this list
    with open("wrong_questions.json", "w") as file:
        json.dump(wrong_questions, file, indent=4)


def load_wrong_questions():
    try:
        with open("wrong_questions.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def load_questions_json():
    try:
        with open("questions.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No questions found")
        return []
        


def view_results():
        try: 
            with open("results.json", "r") as file:
                results = json.load(file)
        except FileNotFoundError:
            print("No previous results found")
            return
        
        if len(results) == 0:
            print("No previous results found")
            
        else:
            print("Previous results: ")
            for result in results:
                print(f"Name: {result.get('name', 'Unknown')}")
                print(f"Score: {result['score']} out of {result['total_questions']}")
                print(f"Selected difficulty: {result['selected_difficulty']}")
                print(f"Wrong catagories: {result['wrong_catagories']}")
                print(f"Wrong difficulties: {result['wrong_difficulties']}")
                print(f"Percentage: {result['percentage']}%")
                print(f"Date taken: {result.get('date_taken', 'Unknown')}")
                print("---")

def questions(name):
    score = 0
    questions_asked = 0
    wrong_questions = []
    wrong_catagories = {}
    wrong_difficulties = {}
    
    selected_difficulty = choose_difficulty()
    quiz_questions = load_questions_json()
    
    for question in quiz_questions:
        question_text = question["question"]
        correct_answer = question["answer"]
        catagory = question["catagory"]
        difficulty = question["difficulty"]
        
    
        if selected_difficulty == "all" or difficulty == selected_difficulty:
            questions_asked += 1

            if ask_question(question_text, correct_answer):
                score += 1
            else:
                wrong_questions.append(question)
            
                if catagory not in wrong_catagories:
                    wrong_catagories[catagory] = 1
                else:
                    wrong_catagories[catagory] += 1
                
                if difficulty not in wrong_difficulties:
                    wrong_difficulties[difficulty] = 1
                else:
                    wrong_difficulties[difficulty] += 1

    total_questions=questions_asked
    print(f"You got {score} out of {total_questions} correct")
    
    if score == total_questions:
        print("Perfect score!")
    elif score >= total_questions / 2:
        print("Good Job, but keep practicing!")
        
    else:
        print("Keep practicing!")
    
    if len(wrong_catagories)==0:
        print("No catagories to review")
    else:
        print("Catagory's to review:")
        for catagory in wrong_catagories:
            print(f"\n-{catagory}: {wrong_catagories[catagory]}")
       
        
    if len(wrong_difficulties)==0:
        print("No difficulties to review")
    else:
        print("\nDifficulties to review:")
        for difficulty in wrong_difficulties:
            print(f"\n-{difficulty}: {wrong_difficulties[difficulty]}")
    
    
    result = build_result(name, score, total_questions, selected_difficulty, wrong_catagories, wrong_difficulties)
    
    save_result_json(result)
    save_wrong_questions(wrong_questions)
    return wrong_questions

def show_weakest_catagories():
    # STEP 1: Load past quiz attempts from the file into a Python list
    try:
        with open("results.json", "r") as file:
            results = json.load(file)
    except FileNotFoundError:
        print("No results found")
        return

    # STEP 2: Empty scoreboard (lives only in memory for this function)
    catagory_totals = {}

    # STEP 3: Walk every past quiz
    for result in results:
        wrong_catagories = result["wrong_catagories"]

        # STEP 4: Walk every category missed in THAT quiz, add into season totals
        for catagory in wrong_catagories:
            count = wrong_catagories[catagory]

            if catagory not in catagory_totals:
                catagory_totals[catagory] = count
            else:
                catagory_totals[catagory] += count

    # STEP 5: If they never missed anything, stop early
    if len(catagory_totals) == 0:
        print("No weak categories yet")
        return

    # STEP 6: Find the category with the highest miss count
    worst_catagory = None
    worst_count = 0

    for catagory in catagory_totals:
        count = catagory_totals[catagory]

        if count > worst_count:
            worst_count = count
            worst_catagory = catagory   # MUST update name AND number together

    # STEP 7: Show the answer + the full breakdown
    print(f"Your weakest category is: {worst_catagory} ({worst_count} missed)")
    print("Weak Category Totals:")
    for catagory in catagory_totals:
        print(f"- {catagory}: {catagory_totals[catagory]} missed")