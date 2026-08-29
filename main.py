# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import json
from tkinter import *
from tkinter import messagebox
import random

def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    number_letters =[random.choice(letters) for i in range(nr_letters)]
    num=[random.choice(numbers) for n in range(nr_numbers)]
    number_symbols=[random.choice(symbols) for sym in range(nr_symbols)]
    password_list=number_letters+num+number_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)# ✅print(password_list)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get().title()
    email=email_entry.get()
    password=password_entry.get()
    new_data= {
        website:{
        "email":email,
        "password":password,
    }}

    if len(website)==0 or password==0:
        messagebox.showerror("Error","Please enter all required information")
    else:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file)
            else:
                data.update(new_data)

                with open("data.json", "w") as data_file:
                        json.dump(data, data_file,indent=4)
            finally:
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)


def final_password():
    website=website_entry.get().title()
    try:
        with open("data.json","r") as data_file:
             data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="Data file not found")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(message=f"email:{email}\npassword:{password}")
        else:
            messagebox.showerror(title="Error",message="Website not found")

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas=Canvas(width=200,height=200)
canvas_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=canvas_img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website")
website_label.grid(row=1,column=0)
email_label=Label(text="Email")
email_label.grid(row=2,column=0)
password_label=Label(text="Password")
password_label.grid(row=3,column=0)
password_label.grid(row=3,column=0)

website_entry=Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"abh123@gmail.com")
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)

search_button=Button(text="Search",command=final_password)
search_button.grid(row=1,column=2)
password_button=Button(text="Generate password",command=gen_pass)
password_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()