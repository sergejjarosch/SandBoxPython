
def chat():
    userEingabe = input("Sag mir Hallo:").lower()
    search = ["hallo", "hi", "grüße", "hello"]

    if userEingabe in search:
        user = input("Hallo, wie heißt du? : ")
        age = input(f"Schön dich kennen zu lernen {user}, wie alt bist du? : ")
        number_age = int(age)
        language = input(f"{user} welche Programmiersprache lernst du gerade? : ")
        if number_age >= 30:
            print(f"{user}, auch mit {age} ist es die richtige Zeit um {language} zu lernen.")
        else:
            print(f"{user}, mit {age} ist es perfect {language} zu lernen.")
    else:
        abschluss_eingabe = input("Sollen wir nochmal beginnen?\n"
                                "ja oder nein? :")
        if "ja" in abschluss_eingabe:
            chat()
        else:
            print("Schönen Tag wünsche ich dir!")

chat()




#TODO optimierte version zu verstehen: