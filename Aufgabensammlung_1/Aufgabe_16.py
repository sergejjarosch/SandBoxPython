"""
Erstellen Sie eine Funktion, die aus eine Liste von Zahlen Einträge entfernt.
Die zu entfernen- den Elemente liegen auch in einer zweiten Liste vor.
Beispielübergabe:
beideListen = [[1, 2, 3],[2]]
Beispielausgabe:
ergebnisListe1 = [1, 3]
Auch mehrfach vorkommende Zahlen werden restlos entfernt:
Beispielübergabe2:
beideListen2 = [[1, 2, 3, 3, 3, 3, 4, 4],[2, 3]]
. Beispielausgabe2:
ergebnisListe12 = [1, 4, 4]

  if item in unsortierte_liste:
        unsortierte_liste.remove(item)
"""

unsortierte_liste = [[1,2,3,3,3,3,4,4,4,4,6,6,6,6], [2,3,3,3]]

# funktioniert bei einfachen Listen.....
# sortierte_liste = list(set(unsortierte_liste))
# bei Listen in Listen, muss es in schleife verpackt werden.

"""In der nächsten Zeile verwenden wir eine List Comprehension, 
um über jede innere Liste der unsortierte_liste zu iterieren:"""

unsortierte_liste = [list(set(item)) for item in unsortierte_liste]

"""
set(item): Wir wandeln jede innere Liste in ein Set um. Dabei werden alle Duplikate entfernt, 
da Sets nur eindeutige Werte enthalten können.

list(set(item)): Wir konvertieren das Set zurück in eine Liste. 
Das Set entfernt die Duplikate, und die Konvertierung zurück in eine Liste stellt sicher, 
dass die Reihenfolge beibehalten wird."""

print(unsortierte_liste)