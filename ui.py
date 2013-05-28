import substitutor
import piCalculator

def tryParseInt(s, base=10):
    try:
        n = int(s, base)
        return True
    except ValueError:
        return False

def getIntInput(prompt):
    s = raw_input(prompt)
    if(tryParseInt(s)):
        return int(s)
    else:
        print "Enter a valid int."
        return getIntInput(prompt)
    
def getYNInput(prompt):
    s = raw_input(prompt)
    if(s.upper() == 'Y' or s.upper() == 'YES'):
        return 'Y'
    elif(s.upper() == 'N' or s.upper() == 'NO'):
        return 'N'
    else:
        print 'Please enter either Y or N.'
        return getYNInput(prompt)

def main():
    word = raw_input('Please enter a word to search: ')
    numDigits = getIntInput('Check how many digits of pi? ')
    pi = piCalculator.pi_chudnovsky(numDigits)
    piString, piDictionary = substitutor.substitutePi(pi)
    if word in piString:
        foundAtIndex = piString.find(word)
        print word + ' was found at ' + str(foundAtIndex)
        print 'Containing String: ' + piString[foundAtIndex-1:foundAtIndex+len(word)+1]
    else:
        print 'Failed to find your word.'
    if(getYNInput('Print your dictionary?') == 'Y'):
        print piDictionary
    if(getYNInput('Print out your Pi String?') == 'Y'):
        print piString
        
main()