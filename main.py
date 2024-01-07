from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    letters_list = [choice(letters) for _ in range(randint(8, 10))]

    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]

    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    generated_password = "".join(password_list)
    password_entry.insert(0, f"{generated_password}")
    pyperclip.copy(generated_password)
# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="ERROR", message="No Data File Found")
    else:
        if website in data.keys():
            messagebox.showinfo(title=f"{website}", message=f"Email {data[website]['email']}\n "
                                                            f"Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No Details for {website} found")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def data_entry():
    website = website_entry.get()
    email = mail_entry.get()
    password = password_entry.get()
    new_data = {
        website:
            {
             "email": email,
             "password": password,
            }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please enter all fields")
    else:
        try:
            with open("data.json", "r") as datafile:
                data = json.load(datafile)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete("0", END)
            password_entry.delete("0", END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

mail_id_label = Label(text="Email/Username:")
mail_id_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_name = StringVar()
website_entry = Entry(width=35, textvariable=website_name)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()


mail_entry = Entry(width=35)
mail_entry.grid(row=2, column=1, columnspan=2)
mail_entry.insert(0, "thanushmaha10@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

generate_button = Button(width=21, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=3)

add_button = Button(width=50, text="Add", command=data_entry)
add_button.grid(row=4, column=1, columnspan=4)

search_button = Button(width=21, text="Search", command=find_password)
search_button.grid(row=1, column=3)

window.mainloop()
