# Napisz program, który pobiera od użytkownika listę liczb naturalnych (oddzielonych pojedyńczą spacją), oraz wypisuje na ekran tą samą listę po usunięciu wszystkich liczb, które spełniają obydwa warunki: są liczbami pierwszymi oraz pojawiają się na liście nieparzystą liczbę razy.

import math
import time
from collections import Counter

inputList = [5, 7, 4, 18, 3, 7, 5, 1, 2, 12, 7, 13 ]
print("Input list:",inputList)
occurDict = Counter(inputList)
n = max(inputList)

# Determination of prime numbers
sqrt_n = math.ceil(math.sqrt(n))
primeList = []
primeList.append(0)
primeList.append(0)
for i in range (2,n+1):
    primeList.append(1)

for i in range (2, sqrt_n):
    if primeList[i] == 1:
        for j in range (i*i, n+1, i):
            primeList[j]=0

# removing duplicated and also prime elements from list
outputList = inputList[:]
for j in inputList:
    if (primeList[j] == 1) and (occurDict[j]%2 == 1):
        outputList.remove(j)

print("Output list:",outputList)
