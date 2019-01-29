# Napisz program przeliczający liczby z dowolnego systemu na dowolny.

# cpnversion from any system to decimal
def fromAnyToDec (value, base):
	if base == 10:
		for ch in value:
			if ch < 48 and ch > 57:
				print('Wartość do konwersji nie jest liczbą dziesiętną!')
				quit()
		return value
	else:
		i = len(value)-1
		result = 0
		for ch in value:
			char = ord(ch)
			if char > 48 and char < 57:
				char -= 48
			elif char > 97 and char < 122:
				char -= 87
			elif char > 65 and char < 90:
				char -= 55
			else:
				print('Wykryto nieprawidłowość w wartości do konwersji! Program zostanie przerwany!')
				quit()

			if char >= base:
				print('Wartość do konwersji jest w innym systemie niż',base,'! Program zostanie przerwany!')
				quit()

			result += char*(base**i)
			i -= 1
		return result

# conversion from decimal on any system
def fromDecToAny (value, base):
	if base == 10:
		return value
	else:
		result = ""
		while (value>0):
			toConv = (value % base)
			if toConv >=0 and toConv < 10:
				toConv += 48
			elif toConv > 9:
				toConv += 87
			result = chr(toConv)+result
			value = int(value/base)
		return result

# flag used for communication with the user
repeat = True

while repeat:
	try:
		baseFrom = int(input('Podaj system z którego następuje konwersja (>=2): '))
		if baseFrom < 2:
			print('Błędne dane!')
			break
		baseTo = int(input('Podaj system docelowy konwersji (>=2): '))
		if baseTo < 2:
			print('Błędne dane!')
			break
		convertedValue = input("Podaj wartość do konwersji: ")
		repeat = False

	except ValueError as ve:
		print('Musisz podać liczbę w formacie dziesiętnym!')
		ans = input('Czy chcesz powtórzyć wprowadzanie danych (T/N)? ')
		if ans == 'N':
			exit

# the main part of the program
decValue = fromAnyToDec(convertedValue, baseFrom)
finalValue = fromDecToAny(decValue, baseTo)
print('Wartość',convertedValue,'po konwersji z systemu',baseFrom,'do systemu',baseTo,'wynosi:',finalValue)
