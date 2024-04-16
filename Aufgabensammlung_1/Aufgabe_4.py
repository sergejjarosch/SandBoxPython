#Zählen Sie die Anzahl der Worte in einem Text und geben Sie diese in einer Ausgabe zurück.

text = "Zählen Sie die Anzahl der Worte in einem Text und geben Sie diese in einer Ausgabe zurück"

char_sum_with_spaces = text.__len__()
ausgabe = text.replace(" ", "")
char_sum_without_spaces = ausgabe.__len__()
print("Die Anzahl der Zeichen, ohne Leerzeichen ist : ", char_sum_without_spaces)
print("Die Anzahl der Zeichen, mit Leerzeichen ist : ", char_sum_with_spaces)