import sqlite3

connect = sqlite3.connect("user.db")
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY ,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
    )''')

users_data = [
   ('Ilimbek', "BERDIEV",2004),
   ('Ilim', "BERDI",2005)
]

for user in users_data:
    cursor.execute("INSERT INTO users (first_name,last_name, age) VALUES (?,?,?)", user) 

cursor.execute("SELECT * FROM users")
info = cursor.fetchall()


print("Список пользователей")
for inf in info:
    print(f"ID {inf[0]} - Имя {inf[1]} - Фамилия {inf[2]} Возраст {inf[3]}")

connect.close()