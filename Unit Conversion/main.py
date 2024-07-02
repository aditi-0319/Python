from tkinter import *

window = Tk()
window.title("Unit Conversion")
window.minsize(width=400, height=150)
window.config(padx=20)

label = Label(text="Convert Miles to Kilometer", font=("Arial", 13, "normal"))
label.grid(column=1, row=0)
label.config(pady=13)

mile_entry = Entry(width=20)
mile_entry.focus()
mile_entry.grid(column=0, row=1)

km_entry = Entry(width=20)
km_entry.insert(END, string="0")
km_entry.grid(column=2, row=1)

equal_label = Label(text="=", font=("Arial", 13, "normal"))
equal_label.grid(column=1, row=1)

mile_label = Label(text="Miles", font=("Arial", 10, "normal"))
mile_label.grid(column=0, row=2)

km_label = Label(text="Km", font=("Arial", 10, "normal"))
km_label.grid(column=2, row=2)


def calculation():
    km_entry.delete(0, END)
    entry = float(mile_entry.get())
    new_input = str(entry*1.609344)
    km_entry.insert(END, string=new_input)
    return new_input


button = Button(text="Calculate", command=calculation)
button.grid(column=1, row=3)

window.mainloop()
