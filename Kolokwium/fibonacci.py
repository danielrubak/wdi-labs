def fib_rek(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rek(n-2)+fib_rek(n-1)

def fib_iter(n):
    if n < 2:
        return 1
    else:
        f1=f2=1
        for i in range(2,n):
            tmp = f1 + f2
            f1 = f2
            f2 = tmp
        return f2

print(fib_rek(7))
print(fib_iter(7))
