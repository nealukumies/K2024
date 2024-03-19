#Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja
# tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä
# lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

def airports_by_type(code, type):
    sql = f"SELECT type, count(*) FROM airport WHERE iso_country='{code}' AND type='{type}' GROUP BY type"
    cursor = connection.cursor()
    cursor.execute(sql)
    result=cursor.fetchall()
    if cursor.rowcount>=1:
        return result

print("Tämä ohjelma kertoo maakoodin perusteella maassa olevien lentokenttien lukumäärät tyypeittäin.")
landcode_input=input("Syötä tähän maakoodi: ")

types=['large_airport', 'medium_airport', 'small_airport', 'closed', 'heliport', 'balloonport', 'seaplane_base']

for item in types:
    item_among_airports=airports_by_type(landcode_input, item)
    if item_among_airports:
        print(f"Tyypin {item} lentokenttiä: {item_among_airports[0][1]}")
    else:
        print(f"Tyypin {item} lentokenttiä ei ole.")