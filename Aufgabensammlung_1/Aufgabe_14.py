"""
Verarbeiten Sie eine übergebende Zahlenfolge mit der Länge 15.
Die Zahlenfolge soll als formatierte Telefonnummer ausgegeben werden.
Beispielübergabe:
        String = „012345678965431“
Beispielausgabe:
        String = „(01234) 567 - 896 543 1“
"""

nummer_eingabe = "012345678965431"

formated_number = "({}) {} - {} {} {}".format(
    nummer_eingabe[:5],
    nummer_eingabe[5:8],
    nummer_eingabe[8:11],
    nummer_eingabe[11:14],
    nummer_eingabe[14:17]
)

print(formated_number)
