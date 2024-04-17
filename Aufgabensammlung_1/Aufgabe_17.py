"""
Entwerfen Sie eine Methode, die einen String so konvertiert, dass der String in lowerCamelCase vorliegt.
 Das bedeutet, dass das erste Word im String kleingeschrieben wird.
 Jedes weitere Word auch klein geschrieben wird, aber der Anfangsbuchstabe ist groß
geschreiben
 Alle Leerzeichen entfernt werden.
Es kann wieder angenommen werden, dass lediglich Leerzeichen zwischen zwei Wörtern ist.
Beispielübergabe:
     String = „Hallo World“
Beispielausgabe:
     String = „halloWorld“
Beispielübergabe2:
String = „Ich kann mit mehreren Worten eine Variabel beschreiben“
Beispielausgabe2:
String = „ichKannMitMehrerenWortenEineVariabelBeschreiben“
"""

eingabe = "Hallo World"
kleine_worte = eingabe.lower().split()
neue_liste =[]

for wort in kleine_worte:
    wort = wort.capitalize()
    neue_liste.append(wort)

formatierte_eingabe = "".join(neue_liste)
formatierte_eingabe = formatierte_eingabe[0].lower() + formatierte_eingabe[1:]

print(formatierte_eingabe)

