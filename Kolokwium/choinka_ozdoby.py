n = 10
counter = 1

for i in range(1, n+1):
    if i%2 == 1:
        if i == 1:
            print(" "*(n-i)+"!")
        else:
            print(" "*(n-i)+"!"+(2*i-3)*'*'+"!")
    else:
        if i == 2:
            print(" "*(n-i)+"*o*")
        else:
            print(" "*(n-i)+"*o"+counter*"***o"+"*")
            counter += 1
