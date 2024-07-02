import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generation():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Invalid Entry", message="Please do not leave any field empty.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

    # output = messagebox.askokcancel(title="Save Data", message=f"Email/Username : {email_entry.get()}\nPassword
    # : " f"{password_entry.get()}\n\nDo you want save the above details?")

    # if output:
    #     with open("data.txt", mode="a") as file:
    #         file.write(f"{website_entry.get()}  |  {email_entry.get()} | {password_entry.get()}\n")
    #         website_entry.delete(0, END)
    #         password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            print(len(data))
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email/Username : {email}\nPassword : {password}")
        else:
            messagebox.showinfo(title="Error", message=f"Details for {website} does not exit.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website : ", font=("Arial", 10, "normal"))
website_label.grid(row=1, column=0)

website_entry = Entry(width=32)
website_entry.focus()
website_entry.get()
website_entry.grid(row=1, column=1)

search = Button(text="Search", width=14, command=find_password)
search.grid(row=1, column=2)

email_label = Label(text="Email/Username : ", font=("Arial", 10, "normal"))
email_label.grid(row=2, column=0)
email_label.config(pady=10)

email_entry = Entry(width=51)
email_entry.insert(0, string="lily261@gmail.com")
email_entry.get()
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password : ", font=("Arial", 10, "normal"))
password_label.grid(row=3, column=0)

password_entry = Entry(width=32)
password_entry.get()
password_entry.grid(row=3, column=1)

generate = Button(text="Generate Password", command=password_generation)
generate.grid(row=3, column=2)

add = Button(text="Add", width=44, command=save_data)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
