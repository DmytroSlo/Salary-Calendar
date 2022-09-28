from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os

logins = ["Yurii.Shvets", "Roman.Tsiura", "Dmytro.Slobodian", "Oksana.Zhambazova"]
passwords = ["D27092022R", "Pknce5h12sd", "1210012255", "101184"]

#функций которые должны производится при вводе логина и пароля
def messagebox1():
    messagebox.showinfo("Проблема авторизации", "Такого акаунта не існує")


def start():
    os.popen("calendar.py")
    root.destroy()
    

def enter():
    if login.get() not in logins:
        messagebox1()
    else:
        start()
    if passwords[logins.index(login)] != password:
        messagebox1()

root = Tk()
root.title("Таргет")
root.geometry("320x420+500+500")
root.resizable(width=False, height=False)
root.iconbitmap(r"logo.ico")

login = tk.StringVar()
password = tk.StringVar()

login_label = Label(text="Login:", font = ("Sylfaen", 10))
password_label = Label(text="Passwodrd:", font = ("Sylfaen", 10))

login_label.pack()
login_label.place(x = 20, y = 20)
password_label.pack()
password_label.place(x = 20, y = 50)

login_entry = Entry(textvariable=login, font = ("Sylfaen", 9))
password_entry = Entry(textvariable=password, show = "*")

login_entry.pack()
login_entry.place(x = 100, y = 20)
password_entry.pack()
password_entry.place(x = 100, y = 50)

message_button = Button(text="Ввійти", font = ("Sylfaen", 10))
message_button.pack()
message_button.place(x = 20, y = 80)
message_button.config(command=enter)


root.mainloop()