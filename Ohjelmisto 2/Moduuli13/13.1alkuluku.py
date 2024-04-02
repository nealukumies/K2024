#Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku
# vai ei. Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
# Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

from flask import Flask, request, Response
import json

app = Flask(__name__)
def primenumber(number):
    if number == 1:
        result = False
    elif number > 1:
        for i in range(2, (number // 2) + 1):
            if (number % i) == 0:
                result = False
                break
            else:
                result = True
    return result


@app.route('/alkuluku/<int:number>')
def check_primenumber(number):
    result = primenumber(number)
    return {"Number": number, "isPrime": result}

@app.errorhandler(404) #jos syöttää muuta kun int
def page_not_found(error):
    response_body = json.dumps({"error": 400, "description": "invalid parameter type"})
    return Response(response=response_body, status=404, mimetype="application/json")

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


