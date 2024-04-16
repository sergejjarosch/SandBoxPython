"""
Finden Sie ein bestimmtes Wort in einem Text. Geben Sie das Wort und die Position an der das Wort beginnt zurück.
Das Wort wird vorher bestimmt oder per Eingabe abgefragt.
Wenn das Wort nicht auftaucht, soll eine entsprechende Meldung zurück gegeben werden.

Beispieleingabe:
Text: „Python is my passion.“ Gesuchte Wort: “my”
Beispielausgabe:
„my gefunden an Stelle 12“

"""
text = "Python is my passion"
search = "bob"


if search in text:
    index = text.index(search)
    print(f"Das Wort {search} konnte an der {index + 1}. Stelle gefunden werden")
else:
    print(f"Das Wort *> {search} <* konnte nicht gefunden werden")
