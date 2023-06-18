## save babynames (extracted previously with regex) to postgres table.

import psycopg2
from baby2008 import babyBoys,babyGirls

#CONNECT TO ALREADY CREATED DATABASE CALLED bincom_test
conn = psycopg2.connect(
	database = 'postgres',
	user = 'postgres',
	password = 'password'
)
conn.autocommit = True
cursor = conn.cursor()

# CREATE A TABLE CALLED babynames
sql_create_table = '''CREATE TABLE babynames
(id serial PRIMARY KEY,
boy_names varchar(15),
girl_names varchar(15));
'''
cursor.execute(sql_create_table)

# INSERT COLOR DATA INTO THE TABLE

for enum,values in enumerate(babyBoys):
	cursor.execute('''INSERT INTO babynames
		(boy_names,girl_names) VALUES(%s,%s)''',(values,babyGirls[enum],))
conn.commit()

cursor.execute('''SELECT * FROM babynames;''')

print("The first 10 results from the db are: ")
for enum,names in enumerate(cursor):
    print(names)
    if enum == 9:
        break
cursor.close()
conn.close()
