from tkinter import *

window = Tk()

window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=100, pady=100)

input = Entry(width=10)
input.grid(row=2, column=2)
#input.config(padx=10, pady=10)


my_label1 = Label(text="Miles", font=("Arial", 24, "italic"))
my_label1.grid(row=2, column=3)

my_label2 = Label(text="is equal to", font=("Arial", 24, "italic"))
my_label2.grid(row=3, column=1)

my_label3 = Label(text="0", font=("Arial", 24, "italic"))
my_label3.grid(row=3, column=2)

my_label4 = Label(text="Km", font=("Arial", 24, "italic"))
my_label4.grid(row=3, column=3)


def button_clicked():
    i = round(int(input.get()) * 1.6)
    my_label3["text"] = i


while True:
    button = Button(text="Calculate", command=button_clicked)
    button.grid(row=4, column=2)


window.mainloop()
