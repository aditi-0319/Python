from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    new_data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/words.csv")
    data = original_data.to_dict(orient="records")
else:
    data = new_data.to_dict(orient="records")

current_card = random.choice(data)


def new_word():
    global current_card

    current_card = random.choice(data)
    card.itemconfig(image, image=card_front_ing)
    card.itemconfig(lang, text="Urdu", fill="black", font=("Arial", 40, "italic"))
    card.itemconfig(word, text=current_card["Urdu"], fill="black")
    window.after(10000, func=flip_card)


def flip_card():
    card.itemconfig(image, image=card_back_ing)
    card.itemconfig(lang, text="English", fill="white")
    card.itemconfig(word, text=current_card["English"], fill="white")


def correct_ans():
    global data

    data.remove(current_card)
    new_data = pandas.DataFrame(data)
    new_data.to_csv("data/words_to_learn.csv")
    new_word()


window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

window.after(10000, func=flip_card)

card = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_ing = PhotoImage(file="./images/card_front.png")
card_back_ing = PhotoImage(file="./images/card_back.png")
image = card.create_image(400, 263, image=card_front_ing)
lang = card.create_text(400, 150, text="Urdu", fill="black", font=("Arial", 40, "italic"))
word = card.create_text(400, 263, text=current_card["Urdu"], fill="black", font=("Arial", 60, "bold"))
card.grid(row=0, column=0, columnspan=2)

wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=new_word)
wrong_button.grid(row=1, column=0)

right_button_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=correct_ans)
right_button.grid(row=1, column=1)

new_word()

window.mainloop()
