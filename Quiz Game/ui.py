from tkinter import  *
from quiz_brain import QuizBrain
from question_model import Question
from data import question_data, logo, science_and_nature, mythology, animal, mathematics, sports, geography

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.wrong = None
        self.right = None
        self.score = None
        self.ques = None
        self.canvas = None
        self.genre = None
        self.question_bank = []
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=40, pady=40, bg=THEME_COLOR)

        self.text = Label(text="Select the quiz category -", bg=THEME_COLOR, font=("Arial", 14, "bold"), fg="white")
        self.text.grid(row=1, column=0)
        # self.text.config(pady=10)
        # self.general_button = Button(text="General", highlightthickness=0, font=("Arial", 10, "bold"), width=25)
        # self.general_button.grid(row=2, column=0)
        # self.science_and_nature_button = Button(text="Science and Nature", highlightthickness=0, font=("Arial", 10, "bold"), width=25)
        # self.science_and_nature_button.grid(row=3, column=0)
        # self.mythology_button = Button(text="Mythology", highlightthickness=0, font=("Arial", 10, "bold"), width=25)
        # self.mythology_button.grid(row=4, column=0)
        # self.animal_button = Button(text="Animal", highlightthickness=0, font=("Arial", 10, "bold"), width=25)
        # self.animal_button.grid(row=5, column=0)
        # self.mathematics_button = Button(text="Mathematics", highlightthickness=0, font=("Arial", 10, "bold"), width=25)
        # self.mathematics_button.grid(row=6, column=0)
        # self.sports_button = Button(text="Sports", highlightthickness=0, font=("Arial", 10, "bold"), width=25)
        # self.sports_button.grid(row=7, column=0)
        # self.geography_button = Button(text="Geography", highlightthickness=0, font=("Arial", 10, "bold"), width=25)
        # self.geography_button.grid(row=8, column=0)

        self.amount = Label(text="Select the number of questions -\nNote : Maximum 10 questions", bg=THEME_COLOR, font=("Arial", 14, "bold"), fg="white")
        self.amount.grid(row=10, column=0)
        self.amount.config(pady=15)

        self.spinbox = Spinbox(from_=0, to=10, width=5, font=("Arial", 10, "normal"))
        self.spinbox.grid(row=11, column=0)

        self.genre_buttons = []
        genres = ["General", "Science and Nature", "Mythology", "Animal", "Mathematics", "Sports", "Geography"]
        for i, genre in enumerate(genres):
            button = Button(text=genre, width=20, command=lambda category=i + 1: self.select_genre(category))
            button.grid(row=1+i, column=0)
            self.genre_buttons.append(button)


        self.window.mainloop()

        # ... Your existing code ...

    def select_genre(self, category: int):
        global question_list, question_bank
        genre_lists = [question_data, science_and_nature, mythology, animal, mathematics, sports, geography]
        question_list = []
        for question in genre_lists[category - 1]:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_list.append(new_question)

        number = min(len(question_list), len(self.question_bank))
        question_bank = random.sample(question_list, number)
        self.quiz_brain = QuizBrain(self.question_bank)
        self.get_next_question()

        # self.get_next_ques()


    def general_button(self):
        self.genre = question_data

        
    def get_next_ques(self):
        self.score = Label(text="Score : 0", bg=THEME_COLOR, font=("Arial", 14, "bold"), fg="white")
        self.score.grid(row=0, column=1)
        
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.ques = self.canvas.create_text(150, 125, width=280, text="Question", font=("Arial", 15, "italic"),
                                            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.canvas.config(bg="white")

        right_img = PhotoImage(file="images/true.png")
        self.right = Button(image=right_img, highlightthickness=0, command=self.tick)
        self.right.grid(row=3, column=0)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong = Button(image=wrong_img, highlightthickness=0, command=self.cross)
        self.wrong.grid(row=3, column=1)
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques, text=q_text)
        else:
            self.canvas.itemconfig(self.ques, text="You have completed the quiz.")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    def tick(self):
        self.feedback(self.quiz.check_answer("True"))

    def cross(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_ques)
