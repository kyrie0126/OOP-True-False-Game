class QuizBrain:

    def __init__(self, question_bank_input):
        self.question_number = 0
        self.question_list = question_bank_input
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        guess = str(input(f"Q{self.question_number}: {current_question.text} (true/false)? ")).lower()
        self.check_answer(guess, current_question.answer)

    def check_answer(self, guess_input, answer_input):
        if guess_input.lower() == answer_input.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {self.question_list[self.question_number-1].answer}.")
        print(f"Your current score is {self.score}/{self.question_number}\n")