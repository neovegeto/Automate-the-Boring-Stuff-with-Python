# In diesem Spiel werden Nummern erraten
import random # Das Modul random importieren

geheimeNummer = random.randint(1,20)
print("Ich denk an eine Nummer zwischen 1 und 20.")

# Der Spieler darf 6 mal raten

for guessTaken in range(1,7,1):
    print("Rate mal")
    guess = int(input())
    if guess < geheimeNummer:
        print("Deine Versuch ist zu niedrig. Dies war dein " + str(guessTaken) + "ter Versuch.")
    elif guess > geheimeNummer:
        print("Dein Versuch is zu hoch. Dies war dein " + str(guessTaken) + "ter Versuch.")
    elif guess == geheimeNummer:
        print("Du hast die Zahl " + str(geheimeNummer) + " erraten. Dies war dein " + str(guessTaken) + "ter Versuch.")
        break
