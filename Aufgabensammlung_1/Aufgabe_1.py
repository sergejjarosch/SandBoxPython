

vocalList = "AaEeIiOoUu"
word = "Momanomimo"

for i in vocalList:
    word = word.replace(i, "")
print(word)


umlaute = "Victor jagt zwölf Boxkämpfer quer über den großen Üsterer Deich."
ausgabe = umlaute.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
print(ausgabe)