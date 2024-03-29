#Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä
# vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan
# dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat
# rajapintapyynnöissä tarvittavan API-avaimen (API key). Selvitä myös, miten saat
# Kelvin-asteet muunnettua Celsius-asteiksi.

import requests
location = input("Enter location: ")

request = "http://api.openweathermap.org/data/2.5/weather?q=" + location + "&APPID=INSERTAPIKEYHERE"

try:
    response = requests.get(request)
    data = response.json()
    if data.get("cod") == "404":
        print("Can´t find location.")
    elif response.status_code == 200:
        print(f"The weather type in {location} is: {data["weather"][0]["main"]}")
        print(f"The temperature is {data["main"]["temp"]-273.15:.2f} Celsius.")
    else:
        print("Error!")

except requests.exceptions.RequestException as e:
    print("API not working.")