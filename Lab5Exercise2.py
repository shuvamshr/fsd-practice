import random


def genRandom():
    myArray = []

    for x in range(20):
        myArray.append(random.randint(0, 100))

    return myArray


def calcMean(anArray):
    return sum(anArray)/len(anArray)


print(calcMean(genRandom()))
