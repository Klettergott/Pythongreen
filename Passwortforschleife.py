Passwort = "Baum"
for i in range(1,6):
    Passwort1 = input("Passwort bitte?: ")
    if Passwort == Passwort1:
        print("\nHerzlich Willkommen!")
        break
    else:
        print("\nFalsches Passwort!")
        print("{}.ter Fehlschlag!\n".format(i))

else:
    print("\nKeine Versuche mehr!")