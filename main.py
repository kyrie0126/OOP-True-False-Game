from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for i in range(0,len(question_data["results"])):
    new_question = Question(question_data["results"][i]["question"], question_data["results"][i]["correct_answer"])
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()


print("You've completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}!")