from random import randint

unsortedList = []
for i in range(1, 6):
    x=randint(1, 50)
    unsortedList.append(x)

def swapElements (listToSort, lowIndex, highIndex):
    listToSort[lowIndex], listToSort[highIndex] = listToSort[highIndex], listToSort[lowIndex]

def bubbleSort(listToSort):
    for i in range(0, len(listToSort)-1):
        print(i)
        for j in range(0, len(listToSort)-1-i):
            if listToSort[j] > listToSort[j+1]:
                swapElements(listToSort, j+1, j)
    return listToSort

print("\nWygenerowana tablica do posortowania:", unsortedList)
print("Sortowanie bąbelkowe:", bubbleSort(unsortedList))
