from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
reps = 0
new_timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(new_timer)
    canvas.itemconfig(timer_text, text="00:00")
    canvas_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def timer():
    global reps, new_timer
    reps += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        countdown(long_break_sec)
        canvas_label.config(text="Break", font=(FONT_NAME, 37, "bold"), bg=YELLOW, fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        canvas_label.config(text="Break", font=(FONT_NAME, 37, "bold"), bg=YELLOW, fg=PINK)
    else:
        countdown(work_sec)
        canvas_label.config(text="Work", font=(FONT_NAME, 37, "bold"), bg=YELLOW, fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global new_timer

    minute = math.floor(count/60)
    second = count % 60
    if minute < 10:
        minute = f"0{minute}"

    if second < 10:
        second = f"0{second}"

    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        new_timer = window.after(1000, countdown, count-1)
    else:
        timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
            check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(height=224, width=220, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(110, 111, image=img)
timer_text = canvas.create_text(110, 130.5, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

canvas_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
canvas_label.grid(column=1, row=0)

start = Button(text="Start", bg=GREEN, font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=timer)
start.grid(column=0, row=3)

reset = Button(text="Reset", bg=GREEN, font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=3)

check_mark = Label(font=(FONT_NAME, 20, "normal"), bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=4)

window.mainloop()
