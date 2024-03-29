#Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin
# käyttäjälle. Käytä seuravalla sivulla esiteltävää rajapintaa:
# https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests

joke_request = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(joke_request)
    if response.status_code==200:
        get_joke = response.json()
        print(get_joke["value"])

except requests.exceptions.RequestException as e:
    print ("Vitsejä ei saatavilla")