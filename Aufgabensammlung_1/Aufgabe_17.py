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

eingabe = "Hallo Alle Zusammen wir werden uns freuen euch zu sehen"
eingabe = eingabe.lower().split()
neue_liste = ""

for wort in eingabe:
    neue_liste += wort.capitalize()

neue_liste = neue_liste[0].lower() + neue_liste[1:]
print(neue_liste)

#-----  title version --------

eingabe_2 ="Hallo Alle Zusammen wir werden uns freuen euch zu sehen"
eingabe_2 = eingabe_2.title().replace(" ","")
eingabe_2 = eingabe_2[0].lower() + eingabe_2[1:]
print(eingabe_2)