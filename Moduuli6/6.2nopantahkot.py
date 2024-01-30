#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan
# maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random
def dice(n):
    value=random.randint(1,n)
    print(value)
    while value<n: #heittää noppaa kunnes silmäluku n
        value=random.randint(1,n)
        print(value)

n=int(input("Syötä tähän noppasi tahkojen lukumäärä: "))

dice(n)