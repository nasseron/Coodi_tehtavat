import mysql.connector

conn = mysql.connector.connect(
     host='127.0.0.1',
     port= 3306,
     database='flight_game',
     user='test',
     password='test',
     autocommit=True
     )

def nimi_ja_sijaintikunta(icao):
     cursor = conn.cursor()

     sql = "select name, municipality from airport"
     sql += f" where ident = '{icao}'"
     cursor.execute(sql)
     result = cursor.fetchall()

     return result

icao = input("Anna lentokentaan icao coodi: ")
result = nimi_ja_sijaintikunta(icao)
print(result)








