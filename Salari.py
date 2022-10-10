import tkinter as tk
import os
import sqlite3
import dbcommand as dc
from tkcalendar import DateEntry, Calendar
import calendar
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import *
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


#Стиль темы
# style = ttk.Style().theme_use()


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


#Валидация
def validation():
    return len(start_box.get()) != 0 and len(finish_box.get()) != 0 and len(work_time_box.get()) != 0


#Добавление
def from_submit():
    if validation():
        Data = data_box.get()
        Start = start_box.get()
        Finish = finish_box.get()
        Work = work_time_box.get()
        Saler = work_time_box.get()
        add_calendar = (Data, Start, Finish, Work, Saler)
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            query = """ INSERT INTO calendar(Дата, Початок_праці, Кінець_праці, Години, Зароблено) 
                                            VALUES (?, ?, ?, ?, (?*22.7)); """
            cursor.execute(query, add_calendar)
            db.commit()

        window.destroy()
        os.popen("Salari.py")
    else:
        msg = "Не всі поля є заповнені"
        mb.showerror("Валідація", msg)

#Редактирование данных

#Валидация
def validation_upgrade():
    return len(start_box_new.get()) != 0 and len(finish_box_new.get()) != 0 and len(work_time_box_new.get()) != 0


def from_update():
    edyt_win = Toplevel()
    edyt_win.title("Изминение данных")
    edyt_win.geometry("330x200")
    edyt_win.resizable(False, False)

    data_new = tk.Label(edyt_win, text = "Дата", font = ("Sylfaen", 12))
    data_new.pack()
    data_new.place(x = 10, y = 10)
    data_box_new = DateEntry(edyt_win, foreground = 'White', normalforeground = 'black',
                                        selectforeground = 'red', beckground = 'white',
                                        date_pattern = 'dd.mm.YYYY', locale="ru", state = 'readonly')
    data_box_new.pack()
    data_box_new.place(x = 150, y = 10)
    start_new = tk.Label(edyt_win, text = "Початок праці", font = ("Sylfaen", 12))
    start_new.pack()
    start_new.place(x = 10, y = 40)
    start_box_new = tk.Entry(edyt_win, font = ("Sylfaen", 10))
    start_box_new.pack()
    start_box_new.place(x = 150, y = 40)
    finish_new = tk.Label(edyt_win, text = "Кінець праці", font = ("Sylfaen", 12))
    finish_new.pack()
    finish_new.place(x = 10, y = 70)
    finish_box_new = tk.Entry(edyt_win, font = ("Sylfaen", 10))
    finish_box_new.pack()
    finish_box_new.place(x = 150, y = 70)
    work_time_new = tk.Label(edyt_win, text = "Години", font = ("Sylfaen", 12))
    work_time_new.pack()
    work_time_new.place(x = 10, y = 100)
    work_time_box_new = tk.Entry(edyt_win, font = ("Sylfaen", 10))
    work_time_box_new.pack()
    work_time_box_new.place(x = 150, y = 100)

    sub = tk.Button(edyt_win, text = "Записати", font = ("Sylfaen", 10), command = upd)
    sub.pack()
    sub.place(x = 10, y = 150)
    
def upd():    
    if validation_upgrade():
        Data_new = data_box_new.get()
        Start_new = start_box_new.get()
        Finish_new = finish_box_new.get()
        Work_new = work_time_box_new.get()
        Saler_new = work_time_box_new.get()
        add_calendar_new = (Data_new, Start_new, Finish_new, Work_new, Saler_new)
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            query = """ UPDATE calendar SET(Дата, Початок_праці, Кінець_праці, Години, Зароблено) 
                                            WHERE (?, ?, ?, ?, (?*22.7)); """
            cursor.execute(query, add_calendar_new)
            db.commit()

        edyt_win.destroy()
        window.destroy()
        os.popen("Salari.py")
    else:
        msg = "Не всі поля є заповнені"
        mb.showerror("Валідація", msg)


ed = tk.Button(frame_statistics, text = "Редагувати", font = ("Sylfaen", 12), command = from_update)
ed.pack()
ed.place(x = 10, y = 140)

#Флажки
r_var = BooleanVar()
r_var.set(0)


#Menu
menu = Menu(window)
new_info = Menu(menu, tearoff = 0)
new_info.add_command(label = 'Info', command = dc.show_info)
new_info.add_separator()
new_info.add_command(label = 'Refresh', command = refresh)
window.bind('<F5>', refresh_bind)
new_info.add_command(label = 'Clear', command = delete_target)
new_info.add_separator()
new_info.add_command(label = 'Export', command = dc.export)
window.bind('<F1>', dc.export_bind)
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
data_box = DateEntry(frame_data, foreground = 'White', normalforeground = 'black',
                                    selectforeground = 'red', beckground = 'white',
                                    date_pattern = 'dd.mm.YYYY', locale="ru", state = 'readonly')
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

submite = tk.Button(frame_data, text = "Записати", font = ("Sylfaen", 12), command = from_submit)
submite.pack()
submite.place(x = 10, y = 140)


#Body statistik
salery = tk.Label(frame_statistics, text = "Зароблено:", font = ("Sylfaen", 12))
salery.pack()
salery.place(x = 10, y = 10)
salery_box = tk.Label(frame_statistics, text = dc.salar, font = ("Sylfaen", 10))
salery_box.pack()
salery_box.place(x = 250, y = 13)


all_time = tk.Label(frame_statistics, text = "Відпрацьовано годин:", font = ("Sylfaen", 12))
all_time.pack()
all_time.place(x = 10, y = 40)
all_time_box = tk.Label(frame_statistics, text = dc.houer, font = ("Sylfaen", 10))
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
lbl.bind("<Button-1>", lambda e: dc.callback("mailto:dmytro.slobodian@reconext.com"))
lbl.place(x = 5, y = 430)


lbl = Label(window, text="form Debug | Repair", font=("Sylfaen", 8))
lbl.pack()
lbl.bind("<Button-1>", lambda e: dc.callback("https://www.reconext.com/"))
lbl.place(x = 590, y = 430)


window.mainloop()