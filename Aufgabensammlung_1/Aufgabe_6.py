"""
Suchen Sie innerhalb eines übergebenen Textes das längste Wort.
Beispieleingabe:
„Die Donaudampfschifffahrtsgesellschaft ist in diesem Beispiel das längste Wort.“
Beispielausgabe: „Donaudampfschifffahrtsgesellschaft“

"""

text = "Die Donaudampfschifffahrtsgesellschaft ist in diesem Beispiel das längste Wort"
woerter = text.split()

laengstes_wort = ""

for wort in woerter:
    if len(wort) > len(laengstes_wort):
        laengstes_wort = wort
print(f"Das längste Wort im Text ist {laengstes_wort}")