# Napisz program wyświetlający animację, której przykład zaprezentowano poniżej. Rozmiar planszy powinien być parametryzowany dwoma liczbami całkowitymi - określającymi szerokość i wysokość (w zaprezentowanym przypadku 11 x 7). W każdej iteracji w górnym wierszu, w losowej kolumnie pojawić się ma jedna kropla - znak X, który w każdym kolejnym kroku powinien przesuwać się o jeden wiersz niżej. Dla uzyskania efektu „animacji” przed wyświetleniem kolejnej iteracji należy czyścić ekran. Proszę odświeżać obraz co 0.3 s. 

import random
import time
import os

random.seed()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

high = int(input('Podaj wysokość planszy: '))
width = int(input('Podaj szerokość planszy: '))

orderList = []

while True:
    n = random.randrange(1+width)
    if len(orderList) < high:
        orderList = [n] + orderList
    elif len(orderList) == high:
        orderList.pop()
        orderList = [n] + orderList

    for j in range (0, len(orderList)):
        print('  '*(orderList[j]-1) + 'X ' + (width-orderList[j])*'  ')
    time.sleep(0.5)
    cls()
