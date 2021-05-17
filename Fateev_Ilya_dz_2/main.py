import tkinter
import numpy as np


def sumOfCardinality(numList):
    theSum = 0
    numbers = []
    for i in numList:
        count = i
        while count > 0:
            numbers.append(count % 10)
            count = count // 10
        if np.sum(numbers) % 7 == 0:
            theSum += i
    return theSum


listOfCubes = []

sumOfCubes = 0

for i in range(1000):
    if i % 2 == 1:
        listOfCubes.append(i ** 3)
print("Sum before changes = ", sumOfCardinality(listOfCubes))

listOfCubes[0:500] = (x + 17 for x in listOfCubes[0:500])
print("Sum after changes = ", sumOfCardinality(listOfCubes))
