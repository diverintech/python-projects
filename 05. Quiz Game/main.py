import art
from data import question_data_general_knowledge, question_data_science_computers
from question_bank import create_question_bank  # Import the function from the new file
from quiz_brain import QuizBrain
from validation import validate_category_choice

"""Display the logo and welcome message"""
print(art.logo)
print("Welcome to the Quiz Game!")
print("You can quit the game at any time by typing 'q'.\n")
print("Please choose a category:")

"""Validate the user's category choice"""
category = validate_category_choice()

""""Set the question data based on the user's category choice"""
if category == "1":
    question_data = question_data_general_knowledge
elif category == "2":
    question_data = question_data_science_computers

"""Create the question bank (list of questions)"""
question_bank = create_question_bank(question_data)

"""Initialize the quiz"""
quiz = QuizBrain(question_bank)
quiz.next_question()

"""Quiz loop while there are still questions remaining"""
while quiz.still_has_questions():
    quiz.next_question()

"""Final message after completing the quiz"""
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
