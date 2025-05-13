import random
#mache eine Funktion, die lottotipps mit Lottozahlen vergleicht und dreier vierer etc. angibt,
#sodass die lottotipps auch mit den Zahlen beim ersten ziehen verglichen werden koennen
def Lottotipps():
    lottotipps = []
    for i in range(6):
        doppelt = True
        while doppelt:
            tipp = int(input("Gib deine Lottotipps ein im Zahlenbereich 1-49!: "))
            print()
            while tipp == 0 or tipp > 49:
                print("Zahl ist außerhalb des Tipp-Bereichs!")
                tipp = int(input("Gib deine Lottotipps ein im Zahlenbereich 1-49!: "))
                print()
            if lottotipps.count(tipp) == 0:
                lottotipps.append(tipp)
                doppelt = False
            else:
                print("{} wurde doppelt eingegeben".format(tipp))
                print()
    lottotipps.sort()
    return lottotipps
def Lottozahlen():
    lottozahlen = []
    print()
    print()
    print("Ziehung der Lottozahlen")
    for i in range(6):
        z = random.randint(1,49)
        lottozahlen.append(z)
        while lottozahlen.count(z) == 2:
            lottozahlen.remove(z)
            z = random.randint(1,49)
            lottozahlen.append(z)
    lottozahlen.sort()
    return lottozahlen

def Vergleich_Lottozahlen(lottotipps,lottozahlen):
    r_lottotipps = []
    for i in range(0,6):
        if lottotipps[i] in lottozahlen:
            r_lottotipps.append(lottotipps[i])
#2 Funktionen erstellen 
#Vergleich Funktion, in die die r_Lottotipps funktion kommt und die sagt, ob man einen dreier, vierer etc. erzielt hat
#so kann man die Vergleiche in jede Lottoziehung über Funktionen implementieren, ohne sich jetzt zum Beispiel für Lottoziehungen und Lottoziehung
#wiederholen zu müssen

    return r_lottotipps

def pruefe_mehrfach_richtig(lottotipps, r_lottotipps,lines,dreier,vierer,fuenfer,sechser):
    if len(r_lottotipps) == 3:
        dreier = dreier + 1
        print(lines)
        print(f"Du hast einen Dreier im Lotto! richtige Zahlen sind {r_lottotipps}, deine Zahlen sind {lottotipps}")
        print(lines)
        print()
    elif len(r_lottotipps) == 4:
        vierer = vierer + 1
        print(lines)
        print(f"Du hast einen Vierer im Lotto! richtige Zahlen sind {r_lottotipps}, deine Zahlen sind {lottotipps}")
        print(lines)
        print()
    elif len(r_lottotipps) == 5:
        fuenfer = fuenfer + 1
        print(lines)
        print(f"Du hast einen Fuenfer im Lotto! richtige Zahlen sind {r_lottotipps}, deine Zahlen sind {lottotipps}")
        print(lines)
        print()
    elif len(r_lottotipps) == 6:
        sechser = sechser + 1
        print(lines)
        print(f"Du hast einen Sechser im Lotto! richtige Zahlen sind {r_lottotipps}, deine Zahlen sind {lottotipps}")
        print(lines)
        print()
    
    return dreier, vierer, fuenfer, sechser,

def Lottoziehungen(lines, r_lottotipps, lottotipps):
    n = int(input("Wie oft soll ich Lottozahlen ziehen lassen und deine Lottotipps auf Dreier, Vierer, Fuenfer und Sechser ueberpruefen?: "))
    for z in range(n + 1):
        neue_lottozahlen = Lottozahlen()
        print()
        print("Neue Lottozahlen: {}".format(neue_lottozahlen))
        korrekt = Vergleich(lottotipps,neue_lottozahlen,dreier,vierer,fuenfer,sechser)
        for i in range(0,6):
            if lottotipps[i] in neue_lottozahlen:
            #b = b + 1
                r_lottotipps.append(lottotipps[i])
        if len(korrekt) == 3:
            dreier = dreier + 1
            print(lines)
            print("3 richtige Zahlen bei Ziehung Nummer {}".format(z))
            print(lottotipps)
            print(lines)
        elif len(r_lottotipps) == 4:
            vierer = vierer + 1
            print(lines)
            print("4 richtige Zahlen bei Ziehung Nummer {}".format(z))
            print(lottotipps)
            print(lines)
        elif len(r_lottotipps) == 5:
            fuenfer = fuenfer + 1
            print(lines)
            print("5 richtige Zahlen bei Ziehung Nummer {}".format(z))
            print(lottotipps)
            print(lines)
        elif len(r_lottotipps) == 6:
            sechser = sechser + 1
            print(lines)
            print("Super! 6 richtige Zahlen bei Ziehung Nummer {}".format(z))
            print(lottotipps)
            print(lines)
    print()
    print("Deine Lottotipps: {}. Du hast: {} Dreier, {} Vierer, {} Fuenfer und {} Sechser erzielt!".format(lottotipps, dreier, vierer, fuenfer, sechser))
    return
def Lottospiel():
    dreier = 0
    vierer = 0
    fuenfer = 0
    sechser = 0
    lines = "-----------------------------------------------"
    lottotipps = Lottotipps()
    r_lottotipps = []
    lottozahlen = Lottozahlen()
    print("deine Lottotipps sind: {}, die Lottozahlen sind: {}".format(lottotipps,lottozahlen))
    Vergleich_Lottozahlen(lottotipps,lottozahlen)
    for i in range(0,6):
        if lottotipps[i] in lottozahlen:
            r_lottotipps.append(lottotipps[i])
    if len(r_lottotipps) > 0:
        print()
        print("Dies sind deine richtigen Lottotipps : {}".format(r_lottotipps))
        Vergleich(lines,lottotipps,lottozahlen,dreier,vierer,fuenfer,sechser)
    elif len(r_lottotipps) == 0:
        print()
        print("Keiner deiner Lottotipps ist richtig")
        print()
    g = int(input("Willst du viele Lottozahlen ziehen lassen und deine Lottotipps auf Dreier, Vierer, Fuenfer, Sechser im Lotto pruefen lassen? Wenn ja gebe '1' ein, ansonsten eine andere Zahl: "))
    if g == 1:
        Lottoziehungen(lines, r_lottotipps, lottotipps)
        print("Danke fuer's Spielen. Bis zum naechsten mal!")
        print()
    else:
        print("Na gut, danke für's Spielen!")

Lottospiel()