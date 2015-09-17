import os
import urllib

def readFile(fname):
    quotesFile = open(fname, "r")
    return quotesFile

def checkProfanity(textLine):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+textLine)
    response = connection.read()
    connection.close()
    return response

def convertPirateSpeech(textLine):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+textLine)
    response = connection.read()
    connection.close()
    return response
    
data = readFile("movie_quotes.txt")
profane = False
for i in data:
    result = checkProfanity(i)
    if "true" in result:
        profane = True
    print(result + ' -- ' + i)

if profane:
    print("You text contains Prafanity. It is advised you proof read before sending it out!")

data.close()

print("BEGIN: Convert Speech to Pirate Language")

data = readFile("Speech.txt")
for i in data:
    result = convertPirateSpeech(i)
    print(result)

data.close()

