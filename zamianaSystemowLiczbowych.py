# toSystem() - zmienia cyfrę na dowolny system (cyfra, system na który zamieniamy)
# toDecimal() - zmiennia cyfrę w dowolnym systemie na liczbę dziesiętną (cyfra, system z krótego zamieniamy)
# changeSystem() - zmienia cyfrę z dowolnego systemu na dowolny system (cyfra, system z którego zamieniamy, system na który chcemy zamienić)

#!  W KODZIE ZAWARTE SĄ ZABEZPIECZENIA PRZED WPISANIEM NIEPRAWIDŁOWYCH DANYCH

import math

def toSystem (number, system):
    if number == False:
        return 'BŁĄD WPISANYCH DANYCH'
    
    result = []
    
    while number >= system:
        result.append(math.floor(number % system))
        
        number = int(math.floor(number) / system)
        
    result.append (number)
    result = result[::-1]
    
    restultString = ''
    
    for i in range(len(result)):
        if result[i] < 10:
            restultString += str(result[i])
        else:
            restultString += chr(55 + result[i])
            
    return restultString

def toDecimal (string, system):
    resultNumber = 0
    string = string[::-1]
    
    for i in range(len(string)):
        if ord(string[i]) >= (48 + system) and system <= 10:
            return False
        if system > 10:
            if ord(string[i]) - 55 >= system:
                return False 
        if ord(string[i]) <= 57:
            resultNumber += int(string[i]) * pow(system, i)
        else:
            resultNumber += int(ord(string[i]) - 55) * pow(system, i)
    
    return resultNumber

def changeSystem (string, systemStart, systemOut):
    if systemStart == 10:
        return toSystem(string, systemOut)
    else:
        return toSystem(toDecimal(string, systemStart), systemOut)

print(changeSystem('5176635', 8, 10))