from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json



# ---------------------------- PASSWORD SEARCH ------------------------------- #

def search_password():
    website = website_entry.get()

    if not website:
        messagebox.showinfo(title="Error", message="Please enter a website")
        return

    try:
        with open("passwords.json", "r") as password_file:
            data = json.load(password_file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showinfo(title="Error", message="No details for this website exist")
        return

    if website not in data:
        messagebox.showinfo(title="Error", message="No details for this website exist")
        return
    else:
        saved_info = data[website]
        email = saved_info["email"]
        password = saved_info["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    password = password_entry.get()
    email = email_username_entry.get()
    password_data = {website: {
        "email": email,
        "password": password,
    }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.askokcancel(title=website, message=f"Your website and password field cannot be empty!")
    else:
        try:
            with open("passwords.json", "r") as password_file:
                data = json.load(password_file)
                data.update(password_data)

        except FileNotFoundError:
            with open("passwords.json", "w") as password_file:
                json.dump(password_data, password_file, indent=4)

        except json.JSONDecodeError:
            with open("passwords.json", "w") as password_file:
                json.dump(password_data, password_file, indent=4)

        else:
           with open("passwords.json", "w") as password_file:
                json.dump(data, password_file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(column=1, row=0)

website = Label(text="Website: ")
website.grid(column=0, row=1)

website_entry = Entry(window, width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
website_entry.focus()

email_username = Label(text="Email/Username: ")
email_username.grid(column=0, row=2)

email_username_entry = Entry(window, width=35)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_username_entry.insert(0, "filip@hotmail.com")

password = Label(text="Password: ")
password.grid(column=0, row=3)

password_entry = Entry(window, width=25)
password_entry.grid(column=1, row=3, sticky="w")

generate_password_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="e")

add_password_button = Button(text="Add", width=45, command=save_password)
add_password_button.grid(column=1, row=4, sticky="w", columnspan=2)

add_search_button = Button(text="Search", command=search_password)
add_search_button.grid(column=2, row=1, sticky="e", columnspan=2)

window.mainloop()