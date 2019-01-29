# Napisz program obliczający pole trójkąta na podstawie długości boków podanych przez użytkownika. 
# Wykorzystaj wzór Herona. Sprawdź poprawność danych pobranych od użytkownika.

import math

a = float(input("Podaj długość pierwszego boku trójkąta: "))
while a<=0:
	print("Długość boku musi być liczbą dodatnią!")
	a = float(input("Podaj długość pierwszego boku trójkąta: "))

b = float(input("Podaj długość drugiego boku trójkąta: "))
while b<=0:
	print("Długość boku musi być liczbą dodatnią!")
	b = float(input("Podaj długość drugiego boku trójkąta: "))

c = float(input("Podaj długość trzeciego boku trójkąta: "))
while c<=0:
	print("Długość boku musi być liczbą dodatnią!")
	c = float(input("Podaj długość trzeciego boku trójkąta: "))

if a<b+c and b<a+c and c<a+b:
	p=1/2*(a+b+c)
	S = math.sqrt(p*(p-a)*(p-b)*(p-c))
	print("Pole trójkąta wynosi:", S) 
else:
	print('Warunki istnienia trójkąta nie zostały spełnione')
