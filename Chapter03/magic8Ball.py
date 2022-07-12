import random # Randomizer importieren
# Funktion erstellen
def getAnswer(answerNumber):
        if answerNumber == 1:
            return 'It is certain'
        elif answerNumber == 2:
            return 'It is decidedly so'
        elif answerNumber == 3:
            return 'Yes'
        elif answerNumber == 4:
            return 'Reply hazy try again'
        elif answerNumber == 5:
            return 'Ask again later'
        elif answerNumber == 6:
            return 'Concentrate and ask again'
        elif answerNumber == 7:
            return 'My reply is no'
        elif answerNumber == 8:
            return 'Outlook not so good'
        elif answerNumber == 9:
            return 'Very doubtful'
# Ausserhalb der Funktion programmieren
r = random.randint(1,9) # Random von 1 bis 9
# Uebergabe der Funktion in eine Variable. Die Funktion wird gleichzeitig mit der Randomizer gefuellt
fortune = getAnswer(r)
# Ausgabe des Ergebnisses
print(fortune)