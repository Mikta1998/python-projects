from tkinter import *

def button_clicked():
    if input_number.get() != "":
        number = input_number.get()
        number = number.replace(" ", "")
        try:
            number = float(number)
            converted_number = round(number * 1.609, 2)
            label_km.config(text=converted_number)
        except ValueError:
            pass

window = Tk()
window.title("Mile to Km Converter")
window.minsize(300, 200)

my_label = Label(text="      ", font=("Arial", 50))
my_label.grid(column=0, row=0)

input_number = Entry(width=10)
input_number.grid(column=1, row=0)

label_1 = Label(text="Miles", font=("Arial", 15))
label_1.grid(column=2, row=0)

label_2 = Label(text="is equal to", font=("Arial", 15))
label_2.grid(column=0, row=1)

label_km = Label(text=0, font=("Arial", 15))
label_km.grid(column=1, row=1)

label_3 = Label(text="Km", font=("Arial", 15))
label_3.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()