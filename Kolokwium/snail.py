distance = 0
h = 10
days = 0
end = False;
x = 4
y = 2
z = 5

while not end:
    distance += x
    if distance%z != 0:
        distance -= y
    days += 1
    if distance > h:
        end = True
print(days)
