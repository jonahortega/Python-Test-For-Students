import review
import quiz

def instructions():
    print("Instructions:")
    print("\nThis is a programming quiz where you will be asked programming and python questions")


def main_menu(questions_func, name):
    last_wrong_questions = []

    while True:
        print("\nMain Menu, select your option:")
        print("1. Start Quiz")
        print("2. View Instructions")
        print("3. Review Missed Questions")
        print("4. View Previous Results")
        print("5. View Weakest Catagories")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            last_wrong_questions = questions_func(name)

        elif choice == "2":
            instructions()

        elif choice == "3":
            wrong_questions = quiz.load_wrong_questions()
            review.review_wrong_questions(wrong_questions)
            
        elif choice == "4":
            quiz.view_results()
            
        elif choice == "5":
            quiz.show_weakest_catagories()

        elif choice == "6":
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, 5, or 6.")