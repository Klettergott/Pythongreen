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

def r_Lottotipps(lottotipps,lottozahlen):
    r_lottotipps = []
    for i in range(0,6):
        if lottotipps[i] in lottozahlen:
            r_lottotipps.append(lottotipps[i])
#2 Funktionen erstellen 
#Vergleich Funktion, in die die r_Lottotipps funktion kommt und die sagt, ob man einen dreier, vierer etc. erzielt hat
#so kann man die Vergleiche in jede Lottoziehung über Funktionen implementieren, ohne sich jetzt zum Beispiel für Lottoziehungen und Lottoziehung
#wiederholen zu müssen

def Lottoziehungen(lottotipps):
    dreier = 0
    vierer = 0
    fuenfer = 0
    sechser = 0
    n = int(input("Wie oft soll ich Lottozahlen ziehen lassen und deine Lottotipps auf Dreier, Vierer, Fuenfer und Sechser ueberpruefen?: "))
    for z in range(n + 1):
        r_lottotipps = []
        neue_lottozahlen = Lottozahlen()
        lines = "-----------------------------------------------"
        print()
        print("Neue Lottozahlen: {}".format(neue_lottozahlen))
        for i in range(0,6):
            if lottotipps[i] in neue_lottozahlen:
            #b = b + 1
                r_lottotipps.append(lottotipps[i])
        if len(r_lottotipps) == 3:
            dreier = dreier + 1
            print(lines)
            print("Super! 3 richtige Zahlen bei Ziehung Nummer {}".format(z))
            print(lottotipps)
            print(lines)
        elif len(r_lottotipps) == 4:
            vierer = vierer + 1
            print(lines)
            print("Super! 4 richtige Zahlen bei Ziehung Nummer {}".format(z))
            print(lottotipps)
            print(lines)
        elif len(r_lottotipps) == 5:
            fuenfer = fuenfer + 1
            print(lines)
            print("Super! 5 richtige Zahlen bei Ziehung Nummer {}".format(z))
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
    lottotipps = Lottotipps()
    r_lottotipps = []
    lottozahlen = Lottozahlen()
    print("deine Lottotipps sind: {}, die Lottozahlen sind: {}".format(lottotipps,lottozahlen))
    for i in range(0,6):
        if lottotipps[i] in lottozahlen:
            r_lottotipps.append(lottotipps[i])
    if len(r_lottotipps) > 0:
        print()
        print("Dies sind deine richtigen Lottotipps : {}".format(r_lottotipps))
    elif len(r_lottotipps) == 0:
        print()
        print("Keiner deiner Lottotipps ist richtig")
        print()
    g = int(input("Willst du viele Lottozahlen ziehen lassen und deine Lottotipps auf Dreier, Vierer, Fuenfer, Sechser im Lotto pruefen lassen? Wenn ja gebe '1' ein, ansonsten eine andere Zahl: "))
    if g == 1:
        Lottoziehungen(lottotipps)
        print("Danke fuer's Spielen. Bis zum naechsten mal!")
        print()
    else:
        print("Na gut, danke für's Spielen!")
Lottospiel()
# als nächstes kannst du die Lottozahlen so oft wie du willst ziehen lassen und
# auf dreier, vierer, fuenfer und sechsen pruefen lassen!
# b = int(input("wie oft willst du sie ziehen lassen?"))
# while b > 0:
# def neue_Lottozahlen mit Listen für alle gezogenen Lottozahlen und pruefe wie oft man
# mehrere richtig hat mit den lottotipps
# b = b - 1
# Variablen für dreier, vierer etc.
