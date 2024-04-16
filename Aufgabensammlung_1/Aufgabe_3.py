
"""
Entwerfen Sie eine alphanumerische Ausgabe.
Das heißt es werden nur Buchstaben und Zah- len ausgegeben.
Entfernen Sie dafür alle Zeichen bis auf Zahlen und Buchstaben aus dem übergebenen Text.

Beispieleingabe:
„Die E-Mail-Adresse der Firma Kimmel & Söhne lautet info@kimmel.org“
Beispielausgabe:
„Die EMailAdresse der Firma Kimmel Söhne lautet infokimmelorg“

"""


sonderzeichen = "@#$%&*+-'()[]{}<>/=!?:;,._|~`"
eingabe = input("Deine Eingabe: ")

for i in sonderzeichen:
    eingabe = eingabe.replace(i,"")
print(eingabe)