Passwort = "Baum"
for i in range(1,6):
    Passwort1 = input("Passwort bitte?: ")
    if Passwort == Passwort1:
        print()
        print("Herzlich Willkommen!")
        break
    else:
        print()
        print("Falsches Passwort!")
        print("{}.ter Fehlschlag!".format(i))
        print()
else:
    print()
    print("Keine Versuche mehr!")