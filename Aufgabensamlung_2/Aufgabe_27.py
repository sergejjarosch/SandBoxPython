"""
Es dürfen nur die String-Methoden „find()“, „rindex()“
verwendet werden. Das bilden eines Substrings kann mittels **> slicing <** erfolgen:
Erstellen Sie eine Lösung mit einer while-Schleife
und ohne die Verwendung von einem Array oder einer Liste.
"""


eingabe_pfad = ("C:/xampp/htdocs/index.html"
                "C:/xampp/htdocs/index.css"
                "C:/xampp/htdocs/uebungen/ue4.html"
                "C:/xampp/htdocs/uebungen/ue3.html"
                "C:/xampp/htdocs/uebungen/ue2.html"
                "C:/xampp/htdocs/uebungen/ue1a.html"
                "C:/xampp/htdocs/uebungen/ue1.html"
                "C:/xampp/htdocs/uebungen/HelloWorld.html"
                )

temp_pfad = ""
header = ""
datei = ""
ausgabe = ""
count = 0

for char in eingabe_pfad:
    if char != "/":
        temp_pfad += char
    else:
        temp_pfad += " "
        count += 1

print(count)
print(temp_pfad)
print(header)

