from random import randint
import time
import xlwt
from tempfile import TemporaryFile
wb = xlwt.Workbook()
ws = wb.add_sheet('Sorting')


while True:
    try:
        listSize = int(input("Podaj rozmiar tablicy (musi być większy od 1): "))
        if listSize < 2:
            print("Wpisano nieprawidłową wartość, sprónuj ponownie!")
            continue
        break
    except ValueError:
        print("Wpisano nieprawidłową wartość, sprónuj ponownie!")

while True:
    try:
        numbLimit = int(input("Podaj największą możliwą liczbę do wylosowania (większą od 10): "))
        if numbLimit < 10:
            print("Wpisano nieprawidłową wartość, sprónuj ponownie!")
            continue
        break
    except ValueError:
        print("Wpisano nieprawidłową wartość, sprónuj ponownie!")

showTimeFlag = 0
while True:
    choice = input("Pokazać czas wykonywania się algorytmów? Wpisz (T/N): ")
    if (choice not in ['T', 't', 'N', 'n']):
        print("Wpisano nieprawidłową wartość, sprónuj ponownie!")
        continue
    elif (choice in ['T', 't']):
        showTimeFlag = 1
    break

saveData = 0
while True:
    choice = input("Przeprowadzić testy z zapisanem danych do .xml? (T/N): ")
    if (choice not in ['T', 't', 'N', 'n']):
        print("Wpisano nieprawidłową wartość, sprónuj ponownie!")
        continue
    elif (choice in ['T', 't']):
        saveData = 1
    break


unsortedList = []
for i in range(listSize):
    x = randint(1, numbLimit)
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

def insertSort(listToSort):
    for i in range(1, len(listToSort)):
        for j in range(i, 0, -1):
            if listToSort[j-1] > listToSort[j]:
                swapElements(listToSort, j-1, j)
    return listToSort

def bubbleSort(listToSort):
    for i in range(0, len(listToSort)-1):
        for j in range(0, len(listToSort)-1-i):
            if listToSort[j] > listToSort[j+1]:
                swapElements(listToSort, j+1, j)
    return listToSort

def quickSort(listToSort, lowIndex, highIndex):
    if ((highIndex - lowIndex) > 0):
        p = partition(listToSort, lowIndex, highIndex)
        quickSort(listToSort, lowIndex, p-1)
        quickSort(listToSort, p+1, highIndex)

def partition(listToSort, lowIndex, highIndex):
    divider = lowIndex
    pivot = highIndex

    for i in range(lowIndex, highIndex):
        if(listToSort[i] < listToSort[pivot]):
            swapElements(listToSort, i, divider)
            divider += 1
    swapElements(listToSort, pivot, divider)
    return divider

def merge(firstList, secondList):
    result = []
    firstList_idx, secondList_idx = 0, 0
    while firstList_idx < len(firstList) and secondList_idx < len(secondList):
        if firstList[firstList_idx]<secondList[secondList_idx]:
            result.append(firstList[firstList_idx])
            firstList_idx += 1
        else:
            result.append(secondList[secondList_idx])
            secondList_idx += 1
    if firstList_idx == len(firstList): result.extend(secondList[secondList_idx:])
    else: result.extend(firstList[firstList_idx:])
    return result

def mergeSort(listToSort):
    if len(listToSort) <=1: return listToSort
    left, right = mergeSort(listToSort[:int(len(listToSort)/2)]), mergeSort(listToSort[int(len(listToSort)/2):])
    return merge(left, right)

def heapify(listToSort, end, i):
    l=2 * i + 1
    r=2 * (i + 1)
    max=i
    if l < end and listToSort[i] < listToSort[l]:
        max = l
    if r < end and listToSort[max] < listToSort[r]:
        max = r
    if max != i:
        swapElements(listToSort, i, max)
        heapify(listToSort, end, max)

def heapSort(listToSort):
    end = len(listToSort)
    start = end // 2 - 1 # use // instead of /
    for i in range(start, -1, -1):
        heapify(listToSort, end, i)
    for i in range(end-1, 0, -1):
        swapElements(listToSort, i, 0)
        heapify(listToSort, i, 0)

# there is need to be different variables for each algorithm
unsortedList_1 = unsortedList[:]
unsortedList_2 = unsortedList[:]
unsortedList_3 = unsortedList[:]
unsortedList_4 = unsortedList[:]
unsortedList_5 = unsortedList[:]
unsortedList_6 = unsortedList[:]

if showTimeFlag == 1:
    # sorting time using select sort method
    start_time = time.clock()
    selectSort(unsortedList_1)
    print("\nCzas trwania sortowania przez wybieranie: ", time.clock()-start_time)
    start_time = time.clock()
    insertSort(unsortedList_2)
    print("Czas trwania sortowania przez wstawianie: ", time.clock()-start_time)
    start_time = time.clock()
    bubbleSort(unsortedList_3)
    print("Czas trwania sortowania bąbelkowego: ", time.clock()-start_time)
    start_time = time.clock()
    quickSort(unsortedList_4, 0, (len(unsortedList_4)-1))
    print("Czas trwania sortowania szybkiego: ", time.clock()-start_time)
    start_time = time.clock()
    sortedList = mergeSort(unsortedList_5)
    print("Czas trwania sortowania przez scalanie: ", time.clock()-start_time)
    start_time = time.clock()
    heapSort(unsortedList_6)
    print("Czas trwania sortowania przez kopcowanie: ", time.clock()-start_time)
elif saveData == 1:
    arraySizes = [100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
    k = 0
    for n in arraySizes:
        print(k)
        print(n)
        unsortedList = []
        for i in range(n):
            x = randint(1, 100)
            unsortedList.append(x)

        unsortedList_1 = unsortedList[:]
        unsortedList_2 = unsortedList[:]
        unsortedList_3 = unsortedList[:]
        unsortedList_4 = unsortedList[:]
        unsortedList_5 = unsortedList[:]
        unsortedList_6 = unsortedList[:]
        ws.write(k, 0, n)

        start_time = time.clock()
        selectSort(unsortedList_1)
        duration = time.clock()-start_time
        ws.write(k, 1, duration)

        start_time = time.clock()
        insertSort(unsortedList_2)
        duration = time.clock()-start_time
        ws.write(k, 2, duration)

        start_time = time.clock()
        bubbleSort(unsortedList_3)
        duration = time.clock()-start_time
        ws.write(k, 3, duration)

        start_time = time.clock()
        quickSort(unsortedList_4, 0, (len(unsortedList_4)-1))
        duration = time.clock()-start_time
        ws.write(k, 4, duration)

        start_time = time.clock()
        sortedList = mergeSort(unsortedList_5)
        duration = time.clock()-start_time
        ws.write(k, 5, duration)

        start_time = time.clock()
        heapSort(unsortedList_6)
        duration = time.clock()-start_time
        ws.write(k, 6, duration)

        k += 1

    wb.save('data.xls')
    wb.save(TemporaryFile())
else:
    # result of sorting
    print("\nWygenerowana tablica do posortowania: ", unsortedList)
    print("Sortowanie przez wybieranie: ", selectSort(unsortedList_1))
    print("Sortowanie przez wstawianie: ", insertSort(unsortedList_2))
    print("Sortowanie bąbelkowe: ", bubbleSort(unsortedList_3))
    quickSort(unsortedList_4, 0, (len(unsortedList_4)-1))
    print("Sortowanie szybkie: ", unsortedList_4)
    sortedList = mergeSort(unsortedList_5)
    print("Sortowanie przez scalanie: ", sortedList)
    heapSort(unsortedList_6)
    print("Sortowanie przez kopcowanie: ", unsortedList_6)
