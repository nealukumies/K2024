#Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun
# taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.
# Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6
# (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien julkaisujen kaikki tiedot
# toteuttamiesi metodien avulla.

class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, pagecount):
        super().__init__(name)
        self.author = author
        self.pagecount = pagecount

    def print_properties(self):
        print(f"Kirjailija: {self.author}, kirja: {self.name}, sivumäärä: {self.pagecount}")
class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_properties(self):
        print(f"Lehti: {self.name}, päätoimittaja: {self.editor}")

publications = []
publications.append(Magazine("Aku Ankka", "Aki Hyyppä"))
publications.append(Book("Hytto n:o 6", "Rosa Liksom", 200))

for publication in publications:
    publication.print_properties()