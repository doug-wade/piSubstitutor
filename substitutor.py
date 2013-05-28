import letterDistribution
import math
import piCalculator

def stripDecimalPoint(numToStrip):
    numStr = str(numToStrip)
    if '.' in numStr:
        piArr = str(numToStrip).split('.')
        return piArr[0] + piArr[1]
    else:
        return numStr

def substitutePi(numericPi=math.pi):
    numToLetterDict = letterDistribution.makeDictionary() 
    stringPi = stripDecimalPoint(numericPi)
    stringPiLen = int(math.floor(len(stringPi) / 2))
    decodedString = ''
    for i in range(stringPiLen):
        dictKey = stringPi[2*i] + stringPi[(2*i)+1]
        decodedString += numToLetterDict[dictKey]
    return decodedString, numToLetterDict