from random import *


def randomArray(length):
    newArray = []
    for i in range(length):
        newArray.append(randint(0, 1000))
    return newArray

def checkSort(array):
    sort = True
    for i in range(len(array)-1):
        if array[i+1] < array[i]:
            sort = False
            break
    return sort

def pleaseSort(array):
    sortedArrayHopefully = randomArray(len(array))
    usedIndexes = []
    maxIndex = len(array) - 1
    for element in array:
        placed = False
        while not placed:
            index = randint(0, maxIndex)
            if index not in usedIndexes:
                usedIndexes.append(index)
                sortedArrayHopefully[index] = element
                placed = True
    return sortedArrayHopefully


yikes = 5
basicArray = randomArray(yikes)
sorted = False
insaneCounter = 0
print("Oh no you've made a mistake choosing this sorting method. You've begun with", basicArray)
print('Yikes level is', yikes)

while not sorted:
    finalArray = pleaseSort(basicArray)
    sorted = checkSort(finalArray)
    insaneCounter += 1


print("Insanity Level reached", insaneCounter, "before arriving at:")
print(finalArray)
