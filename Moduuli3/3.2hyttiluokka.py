#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan,
#tulostaa sen kuvauksen. Käytettävä if/elif/else rakennetta.
#Jos kelvoton hyttiluokka ohjelma tulostaa "Virheellinen hyttiluokka"

print("Tällä ohjelmalla saat laivamatkasi hyttikuvauksen.\n")
hyttiluokka=input("Syötä hyttiluokka LUX, A, B tai C: ")

if hyttiluokka=="LUX" or hyttiluokka=="lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka=="A" or hyttiluokka=="a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka=="B" or hyttiluokka=="b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka=="C" or hyttiluokka=="c":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")