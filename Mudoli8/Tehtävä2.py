import mysql.connector
conn = mysql.connector.connect(
     host='127.0.0.1',
     port= 3306,
     database='flight_game',
     user='test',
     password='test',
     autocommit=True
     )
def count_type(country_code):
    cursor = conn.cursor()
    sql = "select type,count(*) from airport"
    sql += f" where iso_country='{country_code}'"
    sql += " group by type"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

country_code = input("Enter country code: ")
result = count_type(country_code)
print(result)