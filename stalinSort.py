from random import *

def randomArray(length):
    newArray = []
    for i in range(length):
        newArray.append(randint(0, 100000))
    return newArray

def offToGulag(array):
    oldElement = array[0]
    sortedArray = [oldElement]
    for i in range(1, len(array)):
        currentElement = array[i]
        if currentElement >= oldElement:
            sortedArray.append(currentElement)
            oldElement = currentElement
        else:
            gulag.append(currentElement)
    return sortedArray

societyPop = 100000
gulag = []
basicArray = randomArray(societyPop)

finalArray = offToGulag(basicArray)

print("degenerate society is", societyPop)
print("The true Communists working for the bolshevik cause are", finalArray)
print(len(gulag), "capitalist scum have been successfully eliminated")
