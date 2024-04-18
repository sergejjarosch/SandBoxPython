
"""
Erstellen Sie nun eine Kopie von der Python-Datei aus Aufgabenteil
a. Wandeln Sie die Kopie nun so ab, dass beim zusammenfügen die Größe der Elemente beachtet wird.
In der Zielliste sollen die Elemente der Größe nach geordnet sein.
Beispielübergabe:
„[1, 3, 5, 9, 9]“ und „[2, 4, 6, 8, 10]“
Beispielausgabe:
„[1,2,3,4,5,6,8,9,9,10]“
"""

eingabe_1 = [12,1, 3, 5, 9, 9]
eingabe_2 = [8,2, 4, 6, 8, 10, 5 ,8, 9]
ausgabe = []

for num1, num2 in list(zip(eingabe_1, eingabe_2)):
    if num1 < num2:
        ausgabe.append(num1)
        ausgabe.append(num2)
    else:
        ausgabe.append(num2)
        ausgabe.append(num1)

ausgabe.sort()
print(ausgabe)