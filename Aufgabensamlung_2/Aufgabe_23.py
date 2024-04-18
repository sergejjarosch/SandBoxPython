"""
Sie erhalten eine beliebige Liste.
Ordnen Sie die Liste so, dass das kleinste Element in der Rückgabe an vorderster Stelle steht.
Das größte Element soll an letzter Stelle stehen.
"""

eingabeListe = [1,0,4,8,5,3,20,9,0]
min = 0
max = 0
for element in eingabeListe:
    if element > max:
        max = element
    else:
        min = element

if min in eingabeListe:
    index_min = eingabeListe.index(min)
    eingabeListe[0], eingabeListe[index_min] = eingabeListe[index_min], eingabeListe[0]
if max in eingabeListe:
    index_max = eingabeListe.index(max)
    eingabeListe[int(len(eingabeListe)) - 1], eingabeListe[index_max] = eingabeListe[index_max], eingabeListe[int(len(eingabeListe)) - 1]
else:
    print("Die liste ist leer")

print("min = ", min, "max = ", max )
print(eingabeListe)