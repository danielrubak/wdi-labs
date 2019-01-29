# Napisz program przeliczający liczby z systemu dwójkowego na system dziesiątkowy.

binary = input("Podaj ciąg binarny: ")
for c in binary:
	if c not in [0, 1]:
		print("Podano błędne dane wejściowe!")
		break

print('Liczba',binary,'w systemie dzisiętnym wynosi',int(binary,2))
