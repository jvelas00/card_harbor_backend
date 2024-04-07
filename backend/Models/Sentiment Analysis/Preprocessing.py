from nltk.corpus import stopwords
import re

SentimentConverter = {
    "positive": "0",
    "neutral": "1",
    "negative": "2"
}

def ProcessTrainData():
    fileName = "Resources/Datasets/Sentiment Analysis/training.csv"
    outputTrainingFileName = "Models/Sentiment Analysis/Input Files/SentimentAnalysisTrain.txt"
    outputTestFileName = "Models/Sentiment Analysis/Input Files/SentimentAnalysisTest.txt"

    stopWords = set(stopwords.words('english'))

    inputFile = open(fileName, errors='replace')

    lineCounter = 0
    dataList = []

    for line in inputFile:
        tokens = line.split(",")
        sentiment = tokens[2]

        inputString = ""
        for i in range(3, len(tokens)):
            inputString += tokens[i]

        #Removes Special Characters & makes line lowercase
        inputString = re.sub('[^A-Za-z0-9]+', ' ', inputString)
        inputString = inputString.lower()
            
        wordTokens = inputString.split(" ")

        finalString = ""

        for word in wordTokens:
            if word not in stopWords:
                finalWord = re.sub('\W+','', word)
                #Truncates the word down to 12 characters if needed
                finalWord = (word[:12]) if len(word) > 12 else word

                if(finalWord != ''):
                    finalString += finalWord + " "

        #Takes out lines that are empty or only have one word
        #Also takes out lines that are classified as Irrelevant
        if(len(finalString.split(" ")) > 1 and sentiment != "Irrelevant"):

            dataList.insert(lineCounter, SentimentConverter[sentiment.lower()] + "," + finalString + "\n")
            lineCounter += 1

    inputFile.close()

    outputTrainFile = open(outputTrainingFileName, "w")
    outputTestFile = open(outputTestFileName, "w")

    listCounter = 0

    for line in dataList:
        if(listCounter < lineCounter * 0.85):
             outputTrainFile.write(line)
        else:
             outputTestFile.write(line)

        listCounter += 1

def ProcessInput(input):
    stopWords = set(stopwords.words('english'))

    inputString = re.sub('[^A-Za-z0-9]+', ' ', input)
    inputString = inputString.lower()
            
    wordTokens = inputString.split(" ")

    finalString = ""

    for word in wordTokens:
        if word not in stopWords:
            finalWord = re.sub('\W+','', word)
            #Truncates the word down to 12 characters if needed
            finalWord = (word[:12]) if len(word) > 12 else word

            if(finalWord != ''):
                finalString += finalWord + " "

    #Takes out lines that are empty or only have one word
    return finalString

ProcessTrainData()

print(ProcessInput("Man Gearbox really needs to fix this dissapointing drops in the new Borderlands 3 DLC cant be fine to farm bosses on Mayhem 10 to get 1 legendary drop while anywhere else i get 6-10 drops. . Really sucks alot"))