
#TODO Validation implimintieren, input überprüfen. In einer Funkion- strip

faecher = int(input("Anzahl Fächer: "))
schulnoten = []
avg =0

for i in range(faecher):
    schulnoten.append(int(input("Geben Sie die notenein: ")))
    schulnoten
    avg = avg + schulnoten[i]
avg = avg / faecher
print(schulnoten)
print(avg)