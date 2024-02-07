#Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä. Laskenta
# perustuu tietokannasta haettuihin koordinaatteihin. Laske etäisyys geopy-kirjaston avulla

from geopy import distance

import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

def lat_long(code):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{code}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result=cursor.fetchone()
    if cursor.rowcount==1:
        return result

print("Tämä ohjelma laskee kahden lentokentän etäisyyden.")
icao1=input("Syötä lentokentän ICAO-koodi: ")
icao2=input("Syötä toisen lentokentän ICAO-koodi: ")

airport1=(lat_long(icao1))
airport2=(lat_long(icao2))

if airport1 and airport2:
    distance = distance.distance(airport1, airport2).km
    print(f"Lentokenttien etäisyys on {distance:.2f} kilometria.")
else:
    print("Tietoja ei löytynyt.")
