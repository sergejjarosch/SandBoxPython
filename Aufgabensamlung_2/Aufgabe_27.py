"""
Es dürfen nur die String-Methoden „find()“, „rindex()“
verwendet werden. Das bilden eines Substrings kann mittels **> slicing <** erfolgen:
Erstellen Sie eine Lösung mit einer while-Schleife
und ohne die Verwendung von einem Array oder einer Liste.

count = 0

for char in eingabe_pfad:
    if char != "/":
        temp_pfad += char
    else:
        temp_pfad += " "
        count += 1

"""
import os

eingabe_pfad = ("C:/xampp/htdocs/index.html"
                "C:/xampp/htdocs/index.css"
                "C:/xampp/htdocs/uebungen/ue4.html"
                "C:/xampp/htdocs/uebungen/ue3.html"
                "C:/xampp/htdocs/uebungen/ue2.html"
                "C:/xampp/htdocs/uebungen/ue1a.html"
                "C:/xampp/htdocs/uebungen/ue1.html"
                "C:/xampp/htdocs/uebungen/HelloWorld.html"
                )
x = dateiname = os.path.split(eingabe_pfad)
print(x)










"""
aktuell_string = ""
aktuell_ordner = ""
ausgabe = ""

index = 0
while index < len(eingabe_pfad):
    char = eingabe_pfad[index]

    if char == "/":
        while eingabe_pfad[index] != eingabe_pfad[index + 1]:
            aktuell_string += eingabe_pfad[index]
            index += 1

        letzes_slash = aktuell_string.rindex('/')
        dateiname = aktuell_string[letzes_slash + 1:]
        ordner = aktuell_string[: letzes_slash].replace("/", " ")

        ausgabe += dateiname + " " + ordner + "\n"

        aktuell_string = ""
    index += 1

print(ausgabe)
"""

"""
for char in x:
    if char == "/":
        index_header_start = x.find("/",3)
        index_header_end = x.find("/",index_header_start + 1)
        index_file_start = x.find("/",index_header_end)
print(eingabe_pfad[index_header_start + 1 : index_header_end])
print(eingabe_pfad[index_file_start +1 : ])
"""
