import mysql.connector
conn = mysql.connector.connect(
     host='127.0.0.1',
     port= 3306,
     database='flight_game',
     user='test',
     password='test',
     autocommit=True
     )
cursor = conn.cursor()
cursor.execute('SELECT * FROM airport')
items = cursor.fetchall()
for i in items:
     print(i)
