## Build a to-do list in python and use Postgres for persistent storage.

import psycopg2

to_do = []
count = 1

while True:
	todo_length = input('type in the NUMBER (FIGURE) of tasks you want to do for the day: ')
	if todo_length.isdigit(): break
	else: print("Please type in a Number")

todo_length = int(todo_length)
print('type what you want to do for the day.')
while count< todo_length+1:
	print(f"{count}:")
	dailylist = input("")
	to_do.append(dailylist)
	count += 1
print(to_do)

connection = psycopg2.connect(
	database = 'postgres',
	user = 'postgres',
	password = 'password'
)
connection.autocommit = True
cursor = connection.cursor()

# CREATE A TABLE CALLED todo

sql_create_table = '''CREATE TABLE todo
(id serial PRIMARY KEY,
items_todo VARCHAR(255),
item_date DATE NOT NULL DEFAULT CURRENT_DATE);
'''
cursor.execute(sql_create_table)

for value in to_do:
	cursor.execute('''INSERT INTO todo
		(items_todo) VALUES(%s)''',value,)
connection.commit()

for todo in (cursor):
	print(todo)

cursor.close()
connection.close()