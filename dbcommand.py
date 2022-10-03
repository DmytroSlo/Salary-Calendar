import sqlite3
import pandas as pd
import time
import webbrowser
import tkinter as tk
from datetime import date
from tkinter import messagebox as mb


def export_bind(event):
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query = """ SELECT * FROM calendar """
        cursor.execute(query)

    columns = [desc[0] for desc in cursor.description]
    data = cursor.fetchall()
    df = pd.DataFrame(list(data), columns=columns)

    date_string = time.strftime("%d.%m.%Y")
    writer = pd.ExcelWriter('Export/SalariCalendar ' + date_string + '.xlsx')
    df.to_excel(writer, sheet_name='bar')
    writer.save()


    msg = "Файл було успішно експортовано до папки Export яка знаходиться в корені програми."
    mb.showinfo("Експорт данних", msg)


def export():
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query = """ SELECT * FROM calendar """
        cursor.execute(query)

    columns = [desc[0] for desc in cursor.description]
    data = cursor.fetchall()
    df = pd.DataFrame(list(data), columns=columns)

    date_string = time.strftime("%Y-%m-%d")
    writer = pd.ExcelWriter('Export/SalariCalendar ' + date_string + '.xlsx')
    df.to_excel(writer, sheet_name='bar')
    writer.save()


    msg = "Файл було успішно експортовано до папки Export яка знаходиться в корені програми."
    mb.showinfo("Експорт данних", msg)


with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    cursor.execute(""" SELECT SUM(Години) FROM calendar """)
    houer = cursor.fetchone()


with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    cursor.execute(""" SELECT SUM(Зароблено) FROM calendar """)
    salar = cursor.fetchone()


#Funkcional
def callback(url):
    webbrowser.open_new(url)


#Кнопки
def show_info():
    msg = "Ця програма допомагає підраховувати свої години і заробітню плату."
    mb.showinfo("Info", msg)