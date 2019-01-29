# Napisz program przeliczający liczby z systemu dziesiątkowego na dowolny wybrany przez użytkownika. 
# Rozwiąż problem wypisywania cyfr większych niż 9.

try:
	value = int(input('Podaj liczbę: '))
	print("{0:b}".format(value))
except ValueError as ve:
	print(ve)


