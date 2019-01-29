# Fabryka prętów metalowych może sprzedać pręty o długości wyrażonej liczbą naturalną od 1 do 10 m. Przykładowe ceny za pręty odpowiednich długości podane są w liście 'p'. Napisz program, który wczyta od użytkownika liczbę naturalną n oznaczającą długość pręta i poda optymalny sposób pocięcia go, tak aby zmaksymalizować zysk fabryki.

p = [0,1,5,8,9,10,17,17,20,24,30];

n = int(input("Enter the length of the rod:"))
r = [0] * (n+1) # Holds the max revenue of each length
r[1] = p[1]
nodes = [0] * (n+1)
nodes[1] = 1

def cut_rod(n):
    if n == 0:
        q = 0;
    elif n == 1:
        q = p[1];
    else:
        for k in range (1, n+1):
            q = max(r[n], p[k] + cut_rod(n-k))
            if (q>r[n]):
                r[n] = q
                nodes[n] = k
    return q

print("Most profit:",cut_rod(n))
print("How to cut: ", end='');
while n>0:
    print(nodes[n],end=' ')
    n -= nodes[n]
