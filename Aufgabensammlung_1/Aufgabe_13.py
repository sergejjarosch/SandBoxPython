
eingabe_wort = "Ski"
laenge_wort = int(len(eingabe_wort))
median = int(laenge_wort / 2)

if laenge_wort % 2 != 0:
    print(eingabe_wort[median])
else:
    print(eingabe_wort[median - 1], eingabe_wort[median])