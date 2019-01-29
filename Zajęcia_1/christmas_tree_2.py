# Napisz program, który pobiera od użytkownika liczbę n >=1 i rysuje „choinkę”, gdzie ostatnia linia zawiera 2n +1 znaków

n = int(input("Podaj liczbę większą lub równą 1: "))
while n < 1:
	n = int(input("Podane błędnę dane!\nPodaj liczbę większą lub równą 1: "))

for i in range (0, n):
	for j in range (0, 2+i):
		print("  "*(n-j) + "x "*(2*j+1), end="")
		print()
