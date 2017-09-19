targetString = input("Gimme a sentence to encode! ")
encodeValue = int(input("Gimme a number between 1 and 26 to encode by: "))
alphabet = "abcdefghijklmnopqrstuvwxyz"

def makeCipher(encodeValue):
    global ciphAlphabet
    ciphAlphabet = ""
    ciphAlphabet = (alphabet[encodeValue:] + alphabet[:encodeValue])
    return ciphAlphabet

makeCipher(encodeValue)

def encodeString(targetString, ciphAlphabet, alphabet):
    encodeDict = {}
    encodeDict = dict(zip(ciphAlphabet, alphabet))
    global encodedTarget
    encodedTarget = ""
    for ch in targetString.lower():
        if ch in encodeDict:
            encodedTarget += encodeDict[ch]
        else:
            encodedTarget += ch
    return encodedTarget

encodeString(targetString, ciphAlphabet, alphabet)

print(encodedTarget)
