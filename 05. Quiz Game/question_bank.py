from question_model import Question

"""Creates a list of Question objects from the provided question data."""


def create_question_bank(question_data):
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    return question_bank
