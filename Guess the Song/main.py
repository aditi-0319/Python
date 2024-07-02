import time
from song_data import data_60s, data_2000
from art import logo
from model import Question
import random
from brain import Brain

print(logo)

choice = int(input("Choose a decade - \n(1) 60s\n(2) 2000s\nYour choice : "))
if choice == 1:
    chosen_data = data_60s
else:
    chosen_data = data_2000

print("Game starts in 3 seconds.")
time.sleep(3)

score = 0
question_no = 0
question_list = []

for question in chosen_data:
    name = question["name"]
    movie = question["movie"]
    artist = question["artist"]
    location_clip = question["location_clip"]
    location_main = question["location_main"]
    new_question = Question(name, movie, artist, location_clip, location_main)

    all_song_names = [q["name"] for q in chosen_data]
    options = random.sample(all_song_names, 4)
    new_question.options = options

    question_list.append(new_question)
    if 3 <= len(question_list):
        question_bank = random.sample(question_list, 3)


quiz = Brain(question_bank)

while quiz.still_has_questions():
    time.sleep(1)
    quiz.next_question()

print(f"\nYour final score is {quiz.score}/{len(question_bank)}.")
