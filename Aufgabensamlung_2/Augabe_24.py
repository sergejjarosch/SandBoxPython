"""
Sie werden nun eine Liste verarbeiten. Die Liste ist mit ganzen Zahlen gefüllt.
Diese Liste untersuchen Sie und geben Ihre Ergebnisse dann in einem neuer Liste zurück.
Die neue Liste soll nicht die Elemente übernehmen, sondern die Anzahl der größeren Ele- mente.
Zählen Sie wie viele rechte Nachbarn größer sind als das momentane
Element und fügen Sie die Anzahl der neuen Liste hinzu.

Beispielübergabe: „[6,5,7,8,3,9]“
Beispielausgabe: „[3,3,2,1,1,0]“

Die range()-Funktion in Python erzeugt eine Sequenz von Zahlen.
Die Funktion hat drei Argumente: start, stop und step.
Wenn du nur zwei Argumente angibst,
steht das erste für den Startwert und das zweite für den Stopwert.

"""

eingabe = [6,5,7,8,3,9]
ausgabe = []
count = 0

for i in range(len(eingabe)):
    for j in range(i + 1, len(eingabe)): #start = i+1 stop = len(eingabe)
        if eingabe[j] > eingabe[i]:
            count += 1
    ausgabe.append(count)
    count = 0

print(ausgabe)

