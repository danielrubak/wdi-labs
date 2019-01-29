# Napisz program zawierający dwie funkcje: obliczające silnie w sposób rekurencyjny i iteracyjny. Porównaj czasy wykonania
import time
numb = int(input('Podaj liczbę: '))

def rec(n):
    if n <= 1:
        return 1
    else:
        return n*rec(n-1)

def ite(n):
    wynik = 1
    while n>=1:
       wynik *= n
       n -= 1
    return wynik

print("Silnia wyliczona metodą rekurencyjną dla liczby",numb,"wynosi: ", end="")
start_time_rec = time.clock()
print(rec(numb))
diff_time_rec = time.clock()-start_time_rec
print("Silnia wyliczona metodą iteracyjną dla liczby",numb,"wynosi: ", end="")
start_time_ite = time.clock()
print(ite(numb))
diff_time_ite = time.clock()-start_time_ite

print(diff_time_rec, diff_time_ite)
