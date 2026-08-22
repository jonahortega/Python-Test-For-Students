import quiz

def review_wrong_questions(wrong_questions):
    if len(wrong_questions) == 0:
        print("There is nothing to review")
    else:
        review_score = 0

        print("Review your questions you missed: ")

        for question in wrong_questions:
            question_text = question["question"]
            correct_answer = question["answer"]

            if quiz.ask_question(question_text, correct_answer):
                review_score += 1

        print(f"You got {review_score} out of {len(wrong_questions)} review questions correct")