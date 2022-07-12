# Das Modul datetime verfügt über Dienstprogrammfunktionen speziell für Datums- und Uhrzeitmanipulationen in Python

from datetime import datetime
print(datetime.today()) # aktulles Datum anzeigen

# Um das Standardformat für die Datumszeit zu ändern, verwenden Sie das Format strftime und rufen Sie die Methode strftime() auf, die auch im Modul datetime integriert ist.
print(datetime.today().strftime('%Y-%m-%d'))
thisyear = datetime.today().strftime('%Y')
#print(thisyear)
#print(type(thisyear))

# This programm says "Hello" and asks for my name
print("Hello")
print("What is your name?") # Now we have to ask for the name

myName = input() # Variable "myName" and input() to get a prompt for the User

print("It is nice to meet you " + myName)
lenghtmyName = len(myName)

print("The lenght of your name is " + str(lenghtmyName))

print("What is your age?") # Ask for his age

myAge = input() # Variable 'myAge' and input() for the Age of the User
birthyear = int(thisyear) - int(myAge)

print('So you will be ' + str(int(myAge) + 1) + " in a year.")
print('Is it true, that you are born in ' + str(birthyear) + ' ?')