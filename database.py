import sqlite3


with sqlite3.connect('db/database.db') as db:
	cursor = db.cursor()
	query = """ CREATE TABLE IF NOT EXISTS calendar(id INTEGER, Дата INTEGER, Початок_праці INTEGER, Кінець_праці INTEGER, Години INTEGER, Зароблено INTEGER) """
	cursor.execute(query)


with sqlite3.connect('db/database.db') as db:
	cursor = db.cursor()
	query = """ INSERT INTO calendar (Дата, Початок_праці, Кінець_праці, Години, Зароблено)VALUES ('20.09.2022', '06:00', '18:00', '12', '254') """
	query1 = """ INSERT INTO calendar (Дата, Початок_праці, Кінець_праці, Години, Зароблено)VALUES ('21.09.2022', '06:00', '18:00', '12', '254') """
	query2 = """ INSERT INTO calendar (Дата, Початок_праці, Кінець_праці, Години, Зароблено)VALUES ('22.09.2022', '06:00', '18:00', '12', '254') """
	query3 = """ INSERT INTO calendar (Дата, Початок_праці, Кінець_праці, Години, Зароблено)VALUES ('23.09.2022', '06:00', '14:00', '8', '198') """
	query4 = """ INSERT INTO calendar (Дата, Початок_праці, Кінець_праці, Години, Зароблено)VALUES ('24.09.2022', '06:00', '18:00', '12', '254') """
	cursor.execute(query)
	cursor.execute(query1)
	cursor.execute(query2)
	cursor.execute(query3)
	cursor.execute(query4)
	db.commit()