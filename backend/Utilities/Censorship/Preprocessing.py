#This file is used to Take all the innapropriate words, and write them to a new file where they are encrypted
from cryptography.fernet import Fernet

bannedWordsFileName = "Input Files/BannedWords.txt" #Removed for the sake of not having the files in our repository
encryptBannedWordsFileName = "Input Files/EncryptBannedWords.txt"
keyFilePath = "Input Files/EncryptionKey.txt"

bannedWordsFile = open(bannedWordsFileName, errors='replace')
encryptBannedWordsFile = open(encryptBannedWordsFileName, "w")
keyFile = open(keyFilePath, "wb")

key = Fernet.generate_key()
fernet = Fernet(key)

keyFile.write(key)

for line in bannedWordsFile:
    encrypt = fernet.encrypt(bytes(line.strip(), encoding='utf8'))
    encryptBannedWordsFile.write(encrypt.decode())
    encryptBannedWordsFile.write('\n')