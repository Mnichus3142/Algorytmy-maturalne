# cyferki - tablica cyfr do ułożenia, cyfry znajdują się w pliku sortowanieBombelkoweDane.txt, w katalodu pliki
# wynik() - zwraca tablicę ułożonych w kolejności cyfr wraz z czasem trwania procesu

#! CZAS TRWANIA PROCESU NIE JEST OBOWIĄZKOWY

import time

cyferki = open('pliki\sortowanieBombelkoweDane.txt', 'r').read().split('\n')
for i in range(len(cyferki)):
    cyferki[i] = int(cyferki[i])

def wynik (liczby):
    print(sortowanie(liczby))
    print('\nProces trwał: ' + str(time.process_time()) + ' s')

def sortowanie (tablica): 
    global cyferki

    cyferkiRobocze = cyferki

    dlugosc = len(cyferki)

    for j in range(dlugosc, silnia(dlugosc)):
        if sprawdzenie(cyferki):
            return cyferkiRobocze
        else:
            for i in range(len(cyferkiRobocze) - 1):
                if not porownaj(cyferkiRobocze[i], cyferkiRobocze[i + 1]):
                    a = cyferkiRobocze[i]
                    b = cyferkiRobocze[i + 1]
                    cyferkiRobocze[i] = b
                    cyferkiRobocze[i + 1] = a

    return cyferkiRobocze

def sprawdzenie (tablica):
    for i in range(len(tablica) - 1):
        if tablica[i + 1] < tablica[i]:
            return False
    return True

def silnia(cyfra):
    silnia = cyfra
    for i in range(1, cyfra):
        silnia = silnia * i
    return silnia

def porownaj (a, b):
    return a < b

wynik(cyferki)
# print(cyferki)