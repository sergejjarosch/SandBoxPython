
"""
Geben Sie aus einer beliebigen,
gegebener Liste das größte Element zurück.
Verwenden Sie hierzu ausschließlich logischen
Operatoren und keine Funktionen der Liste.
"""

eingabeListe = [5,6,2,3,1,9,15]

max = 0
for element in eingabeListe:
    if element > max:
        max = element
print(max)