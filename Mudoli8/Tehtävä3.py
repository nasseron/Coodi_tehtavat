import mysql.connector
from geopy.distance import geodesic

conn = mysql.connector.connect(
     host='127.0.0.1',
     port= 3306,
     database='flight_game',
     user='test',
     password='test',
     autocommit=True
     )
def airports(icoa):
    cursor = conn.cursor()
    sql = F"select  latitude_deg, longitude_deg from airport where ident='{icoa}'"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
airpor_icoa1 = input("Anna lentokennat:")
cordinater = airports(airpor_icoa1)
airport1_icoa2 = input("Anna lentokennat:")
cordinater1 = airports(airport1_icoa2)
distance = geodesic(cordinater, cordinater1).kilometers
print(distance)