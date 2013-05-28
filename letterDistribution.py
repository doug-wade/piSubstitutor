import random

letterDistribution = {
'a': 8,
'b': 1,
'c': 3,
'd': 4,
'e': 12,
'f': 2,
'g': 2,
'h': 6,
'i': 7,
'j': 1,
'k': 1,
'l': 4,
'm': 2,
'n': 6,
'o': 7,
'p': 2,
'q': 1,
'r': 6,
's': 6,
't': 9,
'u': 3,
'v': 1,
'w': 2,
'x': 1,
'y': 2,
'z': 1
}

def makeDictionary():
    numToLetterDict = {}
    for i in range(100):
        num = str(i)
        if (len(num) < 2):
            num = '0' + num
        chosenLetter = random.choice(letterDistribution.keys())
        countLetter = letterDistribution[chosenLetter]
        countLetter -= 1
        if (countLetter == 0):
            del letterDistribution[chosenLetter]
        else:
            letterDistribution[chosenLetter] = countLetter
        numToLetterDict[num] = chosenLetter
    return numToLetterDict

def testCreation():    
    assignedDictionary = makeDictionary()
    print assignedDictionary['00']
    print assignedDictionary['99']