
nummer_eingabe = "004912345678965431"
nummer_eingabe = nummer_eingabe.replace("00", "+")


formated_number = "{} {} {} - {} {} {}".format(
    nummer_eingabe[:3],
    nummer_eingabe[3:7],
    nummer_eingabe[7:10],
    nummer_eingabe[10:13],
    nummer_eingabe[13:16],
    nummer_eingabe[16:17]
)

print(formated_number)