#Toteutetaan algoritmi piin (π) likiarvon laskemiseksi. Oletetaan, että A on yksikköympyrä eli ympyrä,
# jonka keskipiste on origossa ja jonka säde on yksi. Sen ympärille piirretään pienin mahdollinen neliö B siten,
# että ympyrä A jää kokonaan neliön sisäpuolelle. Neliön nurkkapisteet ovat tällöin (-1,-1), (1,-1), (1,1) ja (-1,1).
# Jos neliön sisälle arvotaan satunnaisesti suuri määrä pisteitä, osuu niistä myös ympyrän sisälle likimain niin suuri
# osuus kuin ympyrän pinta-ala on neliön pinta-alasta eli πr^2/4, joka (koska ympyrän säde on yksi) sievenee muotoon π/4.
# Tästä saadaan yksinkertainen menetelmä piin likiarvon laskemiseksi: Arvotaan neliön B sisälle suuri määrä satunnaisissa
# kohdissa olevia pisteitä, esimerkiksi miljoona. Olkoon N tämä pisteiden kokonaismäärä. Jokaisesta neliön B sisään arvotusta
# pisteestä testataan vuorollaan, jääkö se myös yksikköympyrän A sisälle. Olkoon n ympyrän sisälle jäävien pisteiden kokonaismäärä.
# Nyt pätee n/N≈π/4, josta saadaan π≈4n/N.
# Kirjoita ohjelma, joka kysyy arvottavien pisteiden määrän käyttäjältä ja toteuttaa piin likiarvon laskennan edellä kuvatulla
# menetelmällä. Lopuksi ohjelma tulostaa piin likiarvon käyttäjälle. (Huomaa, että jokaisesta arvotusta pisteestä (x,y) on
# helppoa testata onko se yksikköympyrän A sisällä: riittää testata, toteuttaako piste epäyhtälön x^2+y^2<1.)

# N=pisteiden kokonaismäärä, n=ympyrän sisälle jäävien pisteiden kokonaismäärä
# π≈4n/N
# (x,y) ympyrän sisällä toteutuuko x^2+y^2<1
# neliö b, että ympyrä A jää kokonaan neliön sisäpuolelle

import random
N=int(input("Syötä pisteiden kokonaismäärä: "))
if N<0:
    print("Syötä positiivinen kokonaisluku")
    N = int(input("Syötä pisteiden kokonaismäärä: "))
i=0 #laskuri
n=0 #Eli käyttäjän syöttämä määrä pisteitä (x, y)
while i<=N:
    x=random.uniform(-1, 1)
    y=random.uniform(-1, 1)
    if (x**2+y**2)<1: #tsekkaa onko ympyrässä
        n=n+1
    i=i+1
pii=(4*n)/N

print(f"Pii on {pii}")