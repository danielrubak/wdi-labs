from random import randint

unsortedList = []
for i in range(1, 6):
    x=randint(1, 50)
    unsortedList.append(x)

def swapElements (listToSort, lowIndex, highIndex):
    listToSort[lowIndex], listToSort[highIndex] = listToSort[highIndex], listToSort[lowIndex]

def insertSort(listToSort):
    for i in range(1, len(listToSort)):
        for j in range(i, 0, -1):
            if listToSort[j-1] > listToSort[j]:
                swapElements(listToSort, j-1, j)
    return listToSort

print("\nWygenerowana tablica do posortowania:", unsortedList)
print("Sortowanie przez wybieranie:", insertSort(unsortedList))
