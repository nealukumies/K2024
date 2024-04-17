#Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan
# lentokentän nimen ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä
# lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa:
# http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa:
# {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

import mysql.connector
from flask import Flask

app = Flask(__name__)

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
    result = cursor.fetchone()
    if cursor.rowcount == 1:
        return result

@app.route('/airport/<code>')
def get_airport(code):
    try:
        result = airport_by_code(code)
        return {"ICAO": code, "Name": result[0], "Municipality": result[1]}
    except:
        return {"Error": "Invalid parameters", "Status": 400}

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
