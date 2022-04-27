from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def add_data():
    website_info = website_input.get().lower()
    email_info = email_input.get().lower()
    password_info = password_input.get()
    new_entry = {website_info: {
        "email": email_info,
        "password": password_info,
    }
    }

    if "@" not in email_info or "." not in email_info or len(email_info) == 0:
        messagebox.showinfo(message="Please enter a valid email!")

    if len(email_info) == 0 or len(password_info) == 0:
        messagebox.showinfo(message="Please do not leave any fields empty")

    else:
        messagebox.askokcancel(message=f"are these details correct? Website: {website_info}, Email: {email_info}, Password: {password_info}")
        with open("data.json", "r") as file:
            entry = json.load(file)
            entry.update(new_entry)

        with open("data.json", "w") as file:
            json.dump(entry, file, indent=4)

    website_input.delete(0, END)
    email_input.delete(0, END)
    password_input.delete(0, END)

    website_input.focus()


def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_int = random.randint(1, 7)

    new_letters = [random.choice(letters) for n in range(random_int)]
    new_numbers = [random.choice(numbers) for n in range(random_int)]
    new_symbols = [random.choice(symbols) for n in range(random_int)]

    strong_password = new_letters + new_numbers + new_symbols

    random.shuffle(strong_password)

    password = "".join(strong_password)

    password_input.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(message="Your password has been copied to your clipboard. Feel free to paste it into the website!")


def search():
    with open("data.json", "r") as file:
        data = json.load(file)

        user_website = website_input.get().lower()

        if user_website not in data:
            messagebox.showinfo(message=f"Sorry there is no entry for the website: {user_website.upper()}")
        else:
            wanted_details = data[user_website]
            wanted_email = wanted_details["email"]
            wanted_password = wanted_details["password"]

            messagebox.showinfo(message=f"The associated details for {user_website} are: \n"
                                        f"Email: {wanted_email}, \n"
                                        f"Password: {wanted_password}")


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)


website_input = Entry(width=35)
website_input.grid(row=1, column=1)
website_input.focus()

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.grid(row=2, column=1)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

password_input = Entry(width=35)
password_input.grid(row=3, column=1)

password_button = Button(text="Generate a password", width=15, command=generate_password)
password_button.grid(row=3, column=2)

finished_button = Button(text="Add information", width=33, command=add_data)
finished_button.grid(row=4, column=1)


window.mainloop()