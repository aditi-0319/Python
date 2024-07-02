from playsound import playsound
import random


class Brain:
    def __init__(self, question_bank):
        self.question_no = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        print(f"\nQ{self.question_no}. What song is this from the movie '{current_question.movie}' and sung by "
              f"{current_question.artist}?")
        playsound(current_question.location_clip)

        ans_name = None
        game_on = True
        while game_on:
            ans = int(input("Type 1 to answer the question or type 2 to repeat the clip : "))
            if ans == 1:
                game_on = False
                correct_option = [current_question.name]

                while len(correct_option) < 4:
                    random_option = random.choice(current_question.options)
                    if random_option not in correct_option:
                        correct_option.append(random_option)

                random.shuffle(correct_option)
                correct_index = correct_option.index(current_question.name)

                print("\nOptions:")
                for i, option in enumerate(correct_option):
                    print(f"{i + 1}. {option}")

                ans_name = input("\nYour answer : ")
            else:
                playsound(current_question.location_clip)
        self.check_ans(ans_name, correct_index, current_question)

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def check_ans(self, user_ans, correct_index, current_question):
        user_ans = int(user_ans)
        if user_ans == correct_index + 1:
            self.score += 1
            print("Correct answer!")
        else:
            print("Incorrect answer.")
            print(f"The correct option was {correct_index + 1}.")
        print(f"Your current score is {self.score}/{self.question_no}.")

        ans1 = int(input("Type 1 to play it's longer clip or type 2 to continue : "))
        if ans1 == 1:
            playsound(current_question.location_main)


