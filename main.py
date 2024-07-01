from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank =[]
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("Quiz finished !")
print(f"your final score is {quiz.score}/{quiz.question_number}")True