from random import randint

unsortedList = []
for i in range(1, 6):
    x=randint(1, 50)
    unsortedList.append(x)

def swapElements (listToSort, lowIndex, highIndex):
    listToSort[lowIndex], listToSort[highIndex] = listToSort[highIndex], listToSort[lowIndex]

def selectSort (listToSort):
    for i in range(0, len(listToSort)):
        min = i
        for j in range(i+1, len(listToSort)):
            if listToSort[j] < listToSort[min]:
                min = j
        swapElements(listToSort, i, min)
    return listToSort

print("\nWygenerowana tablica do posortowania:", unsortedList)
print("Sortowanie przez wybieranie:", selectSort(unsortedList))
