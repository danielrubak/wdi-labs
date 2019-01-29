# Napisz prostą grę tekstową. Zadaniem gracza będzie odgadnięcie liczby z zakresu 0-9 wylosowanej przez komputer

import random
random.seed()
losowana = random.randrange(10)

odp = int(input("Podaj liczbe z zakresu 0-9: "))
while odp<0 or odp>9:
	print("Podano błędne dane!")
	odp = int(input("Podaj liczbe z zakresu 0-9: "))


while odp != losowana:
	if odp>losowana:
		odp = int(input("Liczba zbyt duża!\nPodaj kolejną liczbę: "))
	elif odp<losowana:
		odp = int(input("Liczba zbyt mała!\nPodaj kolejną liczbę: "))

print("Gratulacje! Szukaną liczbą była liczba", losowana)

