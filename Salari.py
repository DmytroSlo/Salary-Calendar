import tkinter as tk
import os
import sqlite3
import time
import webbrowser
import pandas as pd
from tkcalendar import DateEntry, Calendar
from datetime import date
from tkinter import ttk
from tkinter import *
from tkinter import Menu
from tkinter import messagebox as mb


#Window
window = Tk()
window.title("Календар")
window.geometry("700x470+800+400")
window.resizable(width=False, height=False)
window.iconbitmap(r"logo.ico")


#Контейнеры
frame_data = tk.Frame(window, width = 350, height = 200)
frame_statistics = tk.Frame(window, width = 350, height = 200)
frame_table = tk.Frame(window, width = 700, height = 300)

frame_data.pack()
frame_data.place(x = 0, y = 0)
frame_statistics.pack()
frame_statistics.place(x = 350, y = 0)
frame_table.pack()
frame_table.place(x = 0, y = 200)


#Funkcional
def callback(url):
    webbrowser.open_new(url)


#Кнопки
def show_info():
    msg = "Ця програма допомагає підраховувати новий таргет і була зроблена для техніків з відділу Debug/Repair"
    mb.showinfo("Info", msg)


#Refresh
def refresh():
    window.destroy()
    os.popen("Salari.py")


#Refresh
def refresh_bind(event):
    window.destroy()
    os.popen("Salari.py")


#exit
def exit_plik():
	window.destroy()


#Блокирование экрана
def block():
    window.attributes("-topmost", True)


#Разблокировка экрана
def unlock():
    window.attributes("-topmost", False)


#Clear
def delete_target():
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query = """ DELETE FROM calendar """
        query1 = """ DELETE FROM sqlite_sequence """
        cursor.execute(query)
        cursor.execute(query1)
        db.commit()

    window.destroy()
    os.popen("Salari.py")
    
    msg = "Всі дані були успішно видалені."
    mb.showinfo("Очистка данних", msg)


#Добавление
def from_submit():
    Data = data_box.get()
    Start = start_box.get()
    Finish = finish_box.get()
    Work = work_time_box.get()
    # Selery = work_time_box.get() * 22,7
    add_calendar = (Data, Start, Finish, Work)
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query = """ INSERT INTO calendar(Дата, Початок_праці, Кінець_праці, Години) 
                                        VALUES (?, ?, ?, ?); """
        cursor.execute(query, add_calendar)
        db.commit()

    window.destroy()
    os.popen("Salari.py")


#Excport
def export():
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query = """ SELECT * FROM calendar """
        cursor.execute(query)

    columns = [desc[0] for desc in cursor.description]
    data = cursor.fetchall()
    df = pd.DataFrame(list(data), columns=columns)

    date_string = time.strftime("%Y-%m-%d")
    writer = pd.ExcelWriter('Export/Targets-' + date_string + '.xlsx')
    df.to_excel(writer, sheet_name='bar')
    writer.save()


    msg = "Файл було успішно експортовано до папки Export яка знаходиться в корені програми."
    mb.showinfo("Експорт данних", msg)


def export_bind(event):
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query = """ SELECT * FROM calendar """
        cursor.execute(query)

    columns = [desc[0] for desc in cursor.description]
    data = cursor.fetchall()
    df = pd.DataFrame(list(data), columns=columns)

    date_string = time.strftime("%d.%m.%Y")
    writer = pd.ExcelWriter('Export/Targets ' + date_string + '.xlsx')
    df.to_excel(writer, sheet_name='bar')
    writer.save()


    msg = "Файл було успішно експортовано до папки Export яка знаходиться в корені програми."
    mb.showinfo("Експорт данних", msg)


def houers():
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query = """ SELECT SUM(Години) FROM calendar """
        cursor.execute(query)


def salari():
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query = """ SELECT SUM(Зароблено) FROM calendar """
        cursor.execute(query)


#Флажки
r_var = BooleanVar()
r_var.set(0)


#Menu
menu = Menu(window)
new_info = Menu(menu, tearoff = 0)
new_info.add_command(label = 'Info', command = show_info)
new_info.add_separator()
new_info.add_command(label = 'Refresh', command = refresh)
window.bind('<F5>', refresh_bind)
new_info.add_command(label = 'Clear', command = delete_target)
new_info.add_separator()
new_info.add_command(label = 'Export', command = export)
window.bind('<F1>', export_bind)
new_info.add_separator()
new_info.add_command(label = "Exit", command = exit_plik)
menu.add_cascade(label = 'File', menu = new_info)


new_comand = Menu(menu, tearoff = 0)
new_comand.add_command(label ='F5                              Refresh')
new_comand.add_command(label = 'F1                              Export')
new_comand.add_command(label = 'Alt + F4                    Exit')
menu.add_cascade(label = 'Commands', menu = new_comand)
window.config(menu = menu)


new_window = Menu(menu, tearoff=0)
block_men = Menu(menu, tearoff=0)
block_men.add_radiobutton(label = "Lock", variable = r_var, value = 1, command = block)
block_men.add_radiobutton(label = 'Unlock', variable = r_var, value = 0, command = unlock)
new_window.add_cascade(label = 'Заблокувати екран', menu = block_men)
menu.add_cascade(label = 'Window', menu = new_window)
window.config(menu = menu)


#Body data
data = tk.Label(frame_data, text = "Дата:", font = ("Sylfaen", 12))
data.pack()
data.place(x = 10, y = 10)
data_box = DateEntry(frame_data, foreground = 'black', normalforeground = 'black',
                                    selectforeground = 'red', beckground = 'white',
                                    date_pattern = 'dd.mm.YYYY', locale="ru")
data_box.pack()
data_box.place(x = 140, y = 15)

start = tk.Label(frame_data, text = "Початок зміни:", font = ("Sylfaen", 12))
start.pack()
start.place(x = 10, y = 40)
start_box = tk.Entry(frame_data, font = ("Sylfaen", 10))
start_box.pack()
start_box.place(x = 140, y = 45)

finish = tk.Label(frame_data, text = "Кінець зміни:", font = ("Sylfaen", 12))
finish.pack()
finish.place(x = 10, y = 70)
finish_box = tk.Entry(frame_data, font = ("Sylfaen", 10))
finish_box.pack()
finish_box.place(x = 140, y = 75)

work_time = tk.Label(frame_data, text = "Разем:", font = ("Sylfaen", 12))
work_time.pack()
work_time.place(x = 10, y = 100)
work_time_box = tk.Entry(frame_data, font = ("Sylfaen", 10))
work_time_box.pack()
work_time_box.place(x = 140, y = 105)

submite = tk.Button(frame_data, text = "Записати", font = ("Sylfaen", 12) , command = from_submit)
submite.pack()
submite.place(x = 10, y = 140)


#Body statistik
salery = tk.Label(frame_statistics, text = "Зароблено:", font = ("Sylfaen", 12))
salery.pack()
salery.place(x = 10, y = 10)
salery_box = tk.Label(frame_statistics, text = salari, font = ("Sylfaen", 10))
salery_box.pack()
salery_box.place(x = 250, y = 13)

all_time = tk.Label(frame_statistics, text = "Відпрацьовано годин:", font = ("Sylfaen", 12))
all_time.pack()
all_time.place(x = 10, y = 40)
all_time_box = tk.Label(frame_statistics, text = houers, font = ("Sylfaen", 10))
all_time_box.pack()
all_time_box.place(x = 250, y = 43)

#Table
class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)
  
        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings
  
        for head in headings:
            table.heading(head, text=head, anchor = 'w')
            table.column(head, anchor= 'w', width = 132, stretch = False)
            table.column('ID', width = 20)        
  
        for row in rows:
            table.insert('', tk.END, values=tuple(row))
  
        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


data = ()
with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM calendar")
    data = (row for row in cursor.fetchall())


table = Table(frame_table, headings=('ID', 'Дата', 'Початок праці', 'Кінець праці', 'Години', 'Зароблено'), rows=data)
table.pack(expand=tk.YES, fill=tk.BOTH)

#Подпись
lbl = Label(window, text="by Dmytro Slobodian", font=("Sylfaen", 8))
lbl.pack()
lbl.bind("<Button-1>", lambda e: callback("mailto:dmytro.slobodian@reconext.com"))
lbl.place(x = 5, y = 430)


lbl = Label(window, text="form Debug | Repair", font=("Sylfaen", 8))
lbl.pack()
lbl.bind("<Button-1>", lambda e: callback("https://www.reconext.com/"))
lbl.place(x = 590, y = 430)


window.mainloop()