"""
Übernehmen Sie aus der vorigen Aufgabensammlung 1 die Aufgaben 7, 8, 9 und 12.
Passen Sie den Quellcode so an, dass keine Ausgabe im Terminal erfolgt,
sondern das Ergebnis der Aufgaben in einer Datei gespeichert wird.


"""

import os


text = ("Am Freitag gibt es viel Sonnenschein und nur lockere Wolken. Im Süden ist es etwas wolkiger"
        "und zu den Alpen hin sind lokale Schauer möglich. 14 bis 25 Grad. Am Samstag ist es trocken und"
        "verbreitet sonnig mit lockeren Quellwolken. Nur an den Alpen entwickeln sich aus dickeren Quellwolken"
        "einzelne Schauer. 15 bis 25 Grad. Am Sonntag ziehen von Norden her im Tagesverlauf"
        "dichtere Wolkenfelder auf, aber nur selten fallen ein paar Regentropfen."
        "In der Südhälfte ist es sonnig und trocken, nur zu den Alpen hin gibt es dickere"
        "Quellwolken mit einzelnen Schauern und Gewittern. 16 bis 27 Grad.")

phrase = text.split(".")
neuer_text = ".\n".join(satz.strip() for satz in phrase)

list = []
for i in phrase:
        list.append(i)
# append fügt die Sätze in die Liste hinzu.

for i in list:
        with open("ausgabe.txt", "w") as datei:
                datei.write(neuer_text)
