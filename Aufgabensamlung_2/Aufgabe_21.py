
"""
Entwerfen Sie ihre eigene split-Methode.
Die Methode iteriert über einen String und speichert jedes Word einzeln in einer Liste.
Es kann davon ausgegangen werden, dass immer genau ein Leerzeichen die Wörter trennt.
Beispielübergabe:
        String = „Hallo World“
Beispielausgabe:
        ergebnisListe = [„Hallo“, „World“]
"""

eingabe = "Hallo World"
wort = ""
ergebnisListe = []


for char in eingabe:
    if char != " ":
        wort += char
    else:
        ergebnisListe.append(wort)
        wort = ""
if wort:
    ergebnisListe.append(wort)

print(ergebnisListe)

