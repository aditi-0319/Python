from question_model import Question
from data import question_data, logo, science_and_nature, mythology, animal, mathematics, sports, geography
from quiz_brain import QuizBrain
import random
from ui import QuizInterface

print(logo)
print(
    "\nSelect the quiz category - \n(1) General\n(2) Science and Nature\n(3) Mythology\n(4) Animal\n(5) "
    "Mathematics\n(6) Sports\n(7) Geography\n\nNote : Maximum 10 questions")
category = int(input("Enter the quiz id : "))
number = int(input("Enter the number of questions : "))

question_list = []
if category == 1:
    genre = question_data
elif category == 2:
    genre = science_and_nature
elif category == 3:
    genre = mythology
elif category == 4:
    genre = animal
elif category == 5:
    genre = mathematics
elif category == 6:
    genre = sports
elif category == 7:
    genre = geography

for question in genre:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_list.append(new_question)
    if number <= len(question_list):
        question_bank = random.sample(question_list, number)

print("Type 'T' for True or type 'F' for False.")

question_bank = random.sample(question_list, number)
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# quiz = QuizBrain(question_bank)
# quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print(f"\nYou have finished the quiz.\nYour final score is {quiz.score}/{len(question_bank)}.")
