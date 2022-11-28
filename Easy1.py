import string

letters = string.ascii_uppercase
encryptMsg = input("encryptMsg: ").upper()#"UFJKXQZQUNB"
key = input("key: ").upper()#"SOLVECRYPTO"


def decrypt(encryptMsg:str, key:str):
    flag = ""
    for i in range(len(encryptMsg)):
        cLetter = encryptMsg[i]
        kLetter = key[i % len(key)]
        clearLetter = letters[(letters.find(cLetter) - letters.find(kLetter)) % len(letters)]
        flag += clearLetter
    print(flag)


def encrypt(encryptMsg:str, key:str):
    flag = ""
    for i in range(len(encryptMsg)):
        cLetter = encryptMsg[i]
        kLetter = key[i % len(key)]
        clearLetter = letters[(letters.find(cLetter) + letters.find(kLetter)) % len(letters)]
        flag += clearLetter
    print(flag)

decrypt(encryptMsg,key)