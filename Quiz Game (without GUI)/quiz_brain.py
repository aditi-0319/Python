import html


class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0
        self.current_question = None

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        print(f"\nQ{self.question_number}. {q_text}. True or False?")
        answer = input("Your answer : ")
        if answer.lower() == "t":
            ans = "True"
        else:
            ans = "False"
        self.check_answer(ans)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        #      OR
        # if self.question_list < len(self.question_list):
        #     return True
        # else:
        #     return False

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            print("Nice! Correct answer!")
        else:
            print("Sorry! Wrong answer!")
            print(f"The correct answer is {correct_answer}.")
        print(f"Current score : {self.score}/{self.question_number}")
