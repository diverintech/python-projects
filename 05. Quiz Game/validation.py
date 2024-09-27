def validate_category_choice():
    while True:
        category = input("Type 1 for General Knowledge or 2 for Science: Computers: ")

        if category == "1" or category == "2":
            return category
        elif category.lower() == "q":
            print("Exiting the game. Goodbye!")
            exit()
        else:
            print("Invalid input. Please enter 1, 2, or 'q' to quit.")


def validate_true_false():
    while True:
        answer = input("Your answer (True/False): ").strip().lower()

        if answer in ["true", "false"]:
            return answer
        elif answer == "q":
            print("Exiting the game. Goodbye!")
            exit()
        else:
            print("Invalid input. Please enter 'True' or 'False'.\n")
