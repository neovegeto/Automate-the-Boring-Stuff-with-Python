''' Write a function named collatz() that has one parameter named number.
If number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1.
'''
# Hint: An integer number is even if number % 2 == 0, and it’s odd if number % 2 == 1.
#
# In dieser Version messen wir noch die benötigte Zeit
from time import time
versuche = 0
t1 = time()
def collatz(number):

    # UnboundLocalError: local variable referenced before assignment
    #  To solve this problem, you can explicitly say  it's a global by putting global declaration in you function.
    global versuche
    # Alternativ --> Return - Statement nutzen
    # write a program that lets the user type in an integer and
    # that keeps calling collatz() on that number until the function returns the value 1.
    while number != 1:
        if number % 2 == 0:
            print(number // 2)
            number = number // 2
            versuche = versuche + 1
        elif number % 2 == 1:
            print( 3 * number + 1)
            number = 3 * number + 1
            versuche = versuche + 1


print("Wir zeigen dir das Wunder von Collatz")
print("Nenn uns eine Zahl mit der wir beginnen sollen")
zahl = int(input())

# Aufrufen der Funktion
collatz(zahl)
t2 = time()
elapsed = t2 - t1

print("Wir haben " + str(versuche) + " Versuche benötigt.")
print('Dafuer haben wir %f Sekunden benoetigt.' % elapsed)
