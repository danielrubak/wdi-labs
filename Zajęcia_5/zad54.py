# Napisz program, który możliwie najefektywniej znajdzie wszystkie liczby pierwsze w zakresie od 1 do max, przyjmij max = 1000. Zmierz czas obliczeń
import math
import time

n = int(input("Podaj liczbę całkowitą większą od 1: "))

start_time = time.time()
sqrt_n = math.ceil(math.sqrt(n))
A = []
A.append(0)
A.append(0)
for i in range (2,n+1):
    A.append(1)

for i in range (2, sqrt_n):
    if A[i] == 1:
        for j in range (i*i, n+1, i):
            A[j]=0

print("--- %s seconds ---" % (time.time() - start_time))

print("Wszystkie liczby pierwsze w przedziale (2, ",n,"):",sep="")
for i in range (2, n+1):
    if A[i]==1:
        print(i)