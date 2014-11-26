__author__ = 'Java'
import string
with open('data1.txt') as source:
    inputString = source.readline().strip()
i = 0
outputString = ""
while i < len(inputString):
    currentLetter = inputString[i]
    currentLetterCount = 0
    j = i + 1
    while j < len(inputString) and inputString[j] in string.digits:
        currentLetterCount = currentLetterCount * 10 + int(inputString[j])
        j += 1
    i = j
    stringForAdd = currentLetter*currentLetterCount
    outputString += stringForAdd
with open('output.txt','w') as out:
    out.write(outputString)





