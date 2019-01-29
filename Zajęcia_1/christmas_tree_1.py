# Napisz program, który pobiera od użytkownika liczbę n >=2 i rysuje „połowę choinki”, gdzie ostatnia linia zawiera n znaków.

n = int(input("Podaj liczbę większą lub równą 2: "))
while n < 2:
	n = int(input("Podane błędnę dane!\nPodaj liczbę większą lub równą 2: "))

for i in range(0, n-1):
    for j in range (0, i+2):
    	print('x '*(j+1), end="")
    	print()