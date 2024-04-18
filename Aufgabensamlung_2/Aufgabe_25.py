"""
Fügen Sie ohne Hilfsmethoden mittels For- oder while-Schleifen zwei Listen zusammen.
Das Resultat hat dann immer abwechselnd eine
Zahl aus der einen Liste und dann gefolgt ein Ele- ment aus der zweiten Liste.

Beispielübergabe:
„[1, 1, 1, 1, 1]“ und „[2, 2, 2, 2, 2]“
Beispielausgabe:
„[1,2,1,2,1,2,1,2,1,2]“

"""

eingabe_1 = [1, 1, 1, 1, 1]
eingabe_2 = [2, 2, 2, 2, 2]
ausgabe = []

for i in range(len(eingabe_1) & len(eingabe_2)):
    ausgabe.append(eingabe_1[i])
    ausgabe.append(eingabe_2[i])
print(ausgabe)