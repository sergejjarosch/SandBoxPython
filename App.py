

"""""
zahl = int (input("Gib deine Zahl ein:"))

if zahl < 4:
    print("Die Zahl ist kleienr 4")
    print(f"Die zahl ist:{zahl}")
else:
    print(f"Die Zahl ist: {zahl}")
    print("Die ist größer als 4...")

"""

meineListe = ["Banane"]
meinTupel = ()
meineMenge = {}

meinDictionary = {
    "name": "Erik",
    "wetter": "sonnig"
}

#append fügt in die liste ein.

meineListe.append("Birne")
print(meineListe)

print("----------- RANGE ------------- ")
zahlenListe = range(10)
print(zahlenListe)

for i in zahlenListe:
    print(i)

print("-------- String -----------")

textZeichenListe = "Aufmerksamkeitsdefizit-Hyperaktivitätsstörung"
for i in textZeichenListe:
    print(i)