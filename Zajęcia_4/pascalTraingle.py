def triangle(k,w):
    if k==1 or k==w :
        return 1
    else:
        return triangle(k-1,w-1)+triangle(k,w-1)

n = 6
for i in range(1,n+1):
    for j in range(1,i+1):
        print(str(triangle(j,i)), end=" ")
    print(" ")
