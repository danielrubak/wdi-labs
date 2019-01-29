n = int(input("Podaj liczbę: "))

print("Wszystkie liczby doskonale z przedzialu 2 do ", n,":", sep='')
for i in range(2,n+1):
    suma = 0
    for j in range (1,i):
        if i%j == 0:
            suma += j
    if suma == i:
        print(i)
