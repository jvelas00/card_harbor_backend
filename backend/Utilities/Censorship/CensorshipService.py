from cryptography.fernet import Fernet

encryptBannedWordsFileName = '../../Utilities/Censorship/Input Files/EncryptBannedWords.txt'
keyFilePath = '../../Utilities/Censorship/Input Files/EncryptionKey.txt'

bannedWordsDict = {}

def ReadFileForKey():
    keyFile = open(keyFilePath, "rb")

    key = b""

    for line in keyFile:
        key = line

    return key

def MakeHashtable(key):
    encryptBannedWordsFile = open(encryptBannedWordsFileName, "r")

    fernet = Fernet(key)
    
    for line in encryptBannedWordsFile:
        bannedWordsDict[fernet.decrypt(line).decode('utf-8')] = False


def CheckCensorship(testString):
    key = ReadFileForKey()
    MakeHashtable(key)

    tokens = testString.split(" ")

    #Simple test to see if the word is in plain text
    for word in tokens:
        if word in bannedWordsDict:
            return True
        
    #Removes all special characters and spaces
    testString = ''.join(letter for letter in testString if letter.isalnum())

    for word in bannedWordsDict:
        if word in testString:
            return True

    return False