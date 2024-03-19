#Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen
# sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)
def airport_by_code(code):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result=cursor.fetchone()
    if cursor.rowcount==1:
        return result

print("Tämä ohjelma kertoo lentoaseman ICAO-koodin perusteella lentoaseman nimen ja sijaintikunnan.")
icao=input("Syötä tähän lentoaseman ICAO-koodi: ")

airport=airport_by_code(icao)
if airport:
    print(f"Lentokenttä {airport[0]} sijaitsee kunnassa {airport[1]}")
else:
    print("Ei tuloksia.")