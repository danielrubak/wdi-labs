# Napisz program obliczający pole trójkąta na podstawie długości boku i wysokości podanej przez użytkownika

a = float(input("Podaj długość boku trójkąta: "))
while a<=0:
	print("Długość boku musi być liczbą dodatnią!")
	a = float(input("Podaj długość boku trójkąta: "))

h = float(input("Podaj wysokość trojkąta: "))
while h<=0:
	print("Wysokość trójkąta musi być liczbą dodatnią!")
	h = float(input("Podaj wysokość trójkąta: "))

pole = 1/2*a*h
print("Pole trójkąta wynosi:", pole)