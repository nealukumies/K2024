#Ohjelma, joka kysyy vuosiluvun ja ilmoittaa onko karkausvuosi
#Karkausvuosi jos jaollinen neljällä.
#Sadalla jaolliset oltava myös jaollisia neljälläsadalla.

print("Tämä ohjelma kertoo onko ilmoittavasi vuosiluku karkausvuosi.")
vuosiluku=int(input("Syötä vuosiluku: "))

if vuosiluku%4==0:
    if vuosiluku%100==0:
        if vuosiluku%400==0:
            print(f"Vuosi {vuosiluku} on karkausvuosi.")
        else:
            print(f"Vuosi {vuosiluku} ei ole karkausvuosi.")
    else:
        print(f"Vuosi {vuosiluku} on karkausvuosi.")
else:
    print(f"Vuosi {vuosiluku} ei ole karkausvuosi.")