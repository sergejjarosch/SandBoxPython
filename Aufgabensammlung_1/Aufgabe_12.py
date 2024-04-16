
#TODO Validation implimintieren, input überprüfen. In einer Funtion- strip

faecher = int(input("Anzahl Fächer: "))
schulnoten = []
avg =0
meinZahlenListe = [0, 1, 2, 3, 4]
meinZahlenListe = range(5)

for i in meinZahlenListe:
    print(i)

for i in meinZahlenListe:
    schulnoten.append(int(input("Geben Sie die notenein: ")))
    print(i)
    avg = avg + schulnoten[i]
print(schulnoten)
print(avg)