
def vocal_konsonant(character):
    vocal = "aouieöäü"
    if character.lower() in vocal:
        print(f"{character} ist ein Vocal")
    else:
        print(f"{character} ist ein Konsonant ")

vocal_konsonant("ü")