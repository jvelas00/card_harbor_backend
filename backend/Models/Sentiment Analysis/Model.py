import tensorflow as tf
from keras import models 
from tensorflow import keras
from keras import layers

from keras.models import Sequential 
from keras.layers import *
from keras.losses import *
from keras.utils import to_categorical
from keras.optimizers import SGD

from numpy import array
import pandas as pd
from keras import preprocessing
import numpy as np

from nltk.tokenize import word_tokenize

MAXDOCLENGTH = 150

Xtrain = []
Ytrain = []
Xtest = []
Ytest = []

wordsList = {}

trainingInputFileName = "Models/Sentiment Analysis/Input Files/SentimentAnalysisTrain.txt"
testingInputFileName = "Models/Sentiment Analysis/Input Files/SentimentAnalysisTest.txt"

trainingInputFile = open(trainingInputFileName, "r")

counter = 1

for line in trainingInputFile:
    line = line.replace("\n","")
    tokens = line.split(",")

    Ytrain.append(int(tokens[0]))

    Xtokens = tokens[1].split(" ")

    tempArray = []
    
    for word in Xtokens:
        if(word != ""):
            if word not in wordsList:
                wordsList[word] = counter
                counter += 1

            tempArray.append(wordsList[word])

    Xtrain.append(tempArray)

trainingInputFile.close()

testingInputFile = open(testingInputFileName, "r")

for line in testingInputFile:
    line = line.replace("\n","")
    tokens = line.split(",")
 
    Ytest.append(int(tokens[0]))

    Xtokens = tokens[1].split(" ")

    tempArray = []
    
    for word in Xtokens:
        if(word != ""):
            if word not in wordsList:
                wordsList[word] = counter
                counter += 1

            tempArray.append(wordsList[word])

    Xtest.append(tempArray)

testingInputFile.close()

X_train = tf.keras.utils.pad_sequences(Xtrain, maxlen=MAXDOCLENGTH)
X_test = tf.keras.utils.pad_sequences(Xtest, maxlen=MAXDOCLENGTH)

X_train = np.array(X_train)
X_test = np.array(X_test)
Y_train = np.array(Ytrain)
Y_test = np.array(Ytest)

Y_train = to_categorical(Ytrain)
Y_test = to_categorical(Ytest)

model = Sequential()
model.add(Embedding( input_dim = counter, output_dim = 100, input_length = MAXDOCLENGTH))
model.add(Bidirectional(SimpleRNN(10, activation = "relu", return_sequences=True)))
model.add(Bidirectional(SimpleRNN(10, activation = "relu")))
model.add(Dense(3, activation="softmax"))
model.compile(
    loss=keras.losses.CategoricalCrossentropy(),
    metrics=['accuracy', keras.metrics.Precision(), keras.metrics.Recall()],
)
model.summary()

model.fit(X_train, Y_train, epochs=10, batch_size=64, validation_split=0.2)

modelOutput = model.save

results = model.evaluate(X_test, Y_test, batch_size=64)