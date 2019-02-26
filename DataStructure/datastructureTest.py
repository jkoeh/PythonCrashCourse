# given a string, find the most appeared character
# ignore white space


def MostCommonChar(inputString):
    inputString=inputString.lower()
    maxDict = {'val':0, 'word': ''}
    lenOfWords=len(inputString)
    wordDictionary={}
    for i in range(lenOfWords):        
        maxVal=maxDict['val']
        maxWord=maxDict['word']
        word = inputString[i]
        if word == " ":
            continue
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1
        if(wordDictionary[word] > maxVal):
            maxDict['val']=wordDictionary[word]
            maxDict['word']=word
        if(maxVal >lenOfWords/2):
            break
    return (maxDict['val'], maxDict['word'])
inputString="What is the most common word in this sentence"
print(MostCommonChar(inputString))