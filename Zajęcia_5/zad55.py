# Napisz program, który możliwie najefektywniej znajdzie wszystkie liczby pierwsze w zakresie od 1 do max, przyjmij max = 1000. Zmierz czas obliczeń
import math
import time
import xlwt

from tempfile import TemporaryFile
wb = xlwt.Workbook()
ws = wb.add_sheet('Duration from value')

k = 0
for n in range (1000000, 10000001, 1000000):
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

    duration = (time.time() - start_time)
    ws.write(k, 0, n)
    ws.write(k, 1, duration)
    k += 1

wb.save('random.xls')
wb.save(TemporaryFile())

