import html

from validation import validate_true_false


class QuizBrain:
    """Manages the quiz game, tracks score, and handles question flow."""

    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        """Displays the next question and checks the user's answer."""
        if self.still_has_questions():
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            print(
                f"Q.{self.question_number}: {html.unescape(current_question.text)} (True/False)"
            )
            user_answer = validate_true_false()
            if user_answer.lower() == "q":
                print("Exiting the game. Goodbye!")
                exit()  # or you could return to main menu or restart
            self.check_answer(user_answer, current_question.answer)
        else:
            print("No more questions available.")
            print(f"Your final score is: {self.score}/{self.question_number}")
            exit()

    def still_has_questions(self):
        """Returns True if there are still questions left, otherwise False."""
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """Checks the user's answer against the correct answer."""
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
