# Napisz kalkulator wykonujący 4 podstawowe działania + potęgowanie

operationList = ['+', '-', '*', '/', '^']

def calculator (first, second, sign):
	if sign == '+':
		print(first,sign,second,'=',(first+second))
	elif sign == '-':
		print(first,sign,second,'=',(first-second))
	elif sign == '*':
		print(first,sign,second,'=',(first*second))
	elif sign == '/':
		try:
			first/second
			print(first,sign,second,'=',(first/second))
		except ZeroDivisionError as zde:
			print(zde)
	elif sign == '^':
		print(first,sign,second,'=',(first**second))


first_numb = int(input('Podaj pierwszą liczbę: '))
second_numb = int(input('Podaj drugą liczbę: '))
operation = input('Podaj rodzaj operacji na wprowadzonych liczbach (+, -, *, /, ^): ')
while (operation not in operationList):
	print('Operacji',operation,'nie ma na liście operacji!')
	operation = input('Podaj rodzaj operacji na wprowadzonych liczbach (+, -, *, /, ^): ')

calculator(first_numb, second_numb, operation)
