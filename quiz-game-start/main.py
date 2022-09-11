from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for current_question in question_data:
    # Loads question data into question_bank
    question_text = current_question["question"]
    question_answer = current_question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed your quiz!")
print(f"You're final score was: {quiz.score}/{quiz.question_number}")
