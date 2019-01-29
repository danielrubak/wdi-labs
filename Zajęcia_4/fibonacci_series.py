#Napisz program obliczający n-ty wyraz ciągu Fibonacciego w sposób rekurencyjny oraz iteracyjny. Porównaj czasy wykonania.

def fibr(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibi(n):
    t=[0, 1]
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        i=2
        while i<=n:
            t.append(t[i-1]+t[i-2])
            i += 1
        return t[n]

print(fibr(9))
print(fibi(9))
