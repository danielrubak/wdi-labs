# Napisz program wyświetlający animację, której przykład zaprezentowano poniżej. Rozmiar planszy powinien być parametryzowany dwoma liczbami nieparzystymi - określającymi szerokość i wysokość (w zaprezentowanym przypadku 11 x 7). Animacja powinna zawierać kwadrat, który od jednego znaku w centrum planszy rozrasta się w każdym kroku, aż nie osiągnie granic planszy, potem zaczyna się kurczyć, do jednego znaku i ponownie rosnąć. Dla uzyskania efektu „animacji” przed wyświetleniem kolejnej iteracji należy czyścić ekran. Proszę odświeżać obraz co 0.3 s.

import random
import math
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

high = int(input('Podaj wysokość planszy: '))
while high <= 0:
	high = int(input('Wysokość planszy nie może być <=0!\nPodaj wysokość planszy: '))
width = int(input('Podaj szerokość planszy: '))
while width <= 0:
	width = int(input('Szerokość planszy nie może być <=0!\nPodaj wysokość planszy: '))

grow_flag = 1 #if grow_flag is equal 1 it means that the square grow
positionInfo = [] # contains the position of the center of the figure ant its radius
currentRadius = 0

if (high % 2) == 0:
	positionInfo.append(int((high-1)/2))
else:
	positionInfo.append(int(high/2)+1)
if (width % 2) == 0:
	positionInfo.append(int((width-1)/2))
else:
	positionInfo.append(int(width/2)+1)
positionInfo.append(min(high-positionInfo[0], width-positionInfo[1]))

while True:
	for i in range (0, high+2):
		if i == 0 or i == high+1:
			print('-'*(width+2),end="")
		for j in range (0, width+2):
			if (i!=0 and i!=high+1) and (j==0 or j==width+1):
				print('|',end="")
			else:
				if max((math.fabs(i-positionInfo[0])),(math.fabs(j-positionInfo[1]))) == currentRadius:
					print('X',end="")
				else:
					print(' ',end="")
		print()

	if currentRadius == positionInfo[2]:
		grow_flag = 0
	elif currentRadius == 0:
		grow_flag = 1
	if grow_flag == 1:
		currentRadius += 1
	else:
		currentRadius -= 1
	time.sleep(0.5)
	cls()
