import quiz
import menu

def user():
    print("welcome to the quiz game!")
    name = input("What is your name? ")
    print(f"\nHello {name}, let's play!")
    return name  # give the name back to whoever called user()


if __name__ == "__main__":
    name = user()  # catch the returned name in a variable
    menu.main_menu(quiz.questions, name)  # hand it to the menu
