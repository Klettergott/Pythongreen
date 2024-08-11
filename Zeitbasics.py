import time
import datetime
import threading
# 1. Zeitverzoegerung mit time.sleep()
def delay_example():
    print("Start der Verzoegerung...")
    time.sleep(3) # 3 Sekunden warten
    print("3 Sekunden spaeter")

# 2. aktuelle Uhrzeit und Datum mit date.time
def current_time_date():
    now = datetime.datetime.now()
    print(f"aktuelle Zeit: {now.strftime('%H:%M:%S')}")
    print(f"aktuelles Datum: {now.strftime('%d.%m.%Y')}")

# 3. Countdown-Timer
def countdown(seconds):
    print("Countdown startet...")
    while seconds > 0:
        print(f"verbleibende Zeit: {seconds} Sekunden")
        time.sleep(1)
        seconds -= 1
    print("Countdown beendet!")

# 4. Timer-Funktion mit threading.Timer
def timer_function():
    print("Timer gestartet... 5 Sekunden bis zur Ausfuehrung")
    t = threading.Timer(5.0, timer_message) # 5 Sekunden Verzoegerung
    t.start()
def timer_message():
    print("Timer ausgefuehrt!")

#Hauptprogramm
def main():
    print("1. Zeitverzoegerung Beispiel: ")
    delay_example()

    time.sleep(2)
    print("\n2. aktuelle Zeit und Datum: ")
    current_time_date()

    time.sleep(2)
    print("\n3. Countdown Timer Beispiel (10 Sekunden): ")
    countdown(10)

    time.sleep(2)
    print("\n4. Timer-Funktion Beispiel: ")
    timer_function()

    print("\n das Hauptprogramm wartet auf den Timer (5 Sekunden)...")
    time.sleep(6) # wartet lange genug, damit der Timer ausgefuehrt wird

if __name__ == "__main__":
    main()