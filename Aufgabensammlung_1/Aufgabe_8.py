"""
Lesen Sie einen übergebenen Text ein und speichern Sie den Text in einer Liste.
Jeden Satz soll in der Liste einen eigenen Index erhalten.
Beispielübergabe:
Sie können den Text aus Aufgabe 7 verwenden.

"""

from colorama import init, Fore
init()

text = ("Am Freitag gibt es viel Sonnenschein und nur lockere Wolken. Im Süden ist es etwas wolkiger"
        "und zu den Alpen hin sind lokale Schauer möglich. 14 bis 25 Grad. Am Samstag ist es trocken und"
        "verbreitet sonnig mit lockeren Quellwolken. Nur an den Alpen entwickeln sich aus dickeren Quellwolken"
        "einzelne Schauer. 15 bis 25 Grad. Am Sonntag ziehen von Norden her im Tagesverlauf"
        "dichtere Wolkenfelder auf, aber nur selten fallen ein paar Regentropfen."
        "In der Südhälfte ist es sonnig und trocken, nur zu den Alpen hin gibt es dickere"
        "Quellwolken mit einzelnen Schauern und Gewittern. 16 bis 27 Grad.")

phrases = text.split(".")

list = []

for i in phrases:
    list.append(i)
# append fügt die Sätze in die Liste hinzu.

for i in list:
    print(Fore.BLUE + "-------> Satz Index Nr. :", list.index(i), "<-------")
    print(Fore.LIGHTWHITE_EX +list[list.index(i)])
