
target = "Encode! this sentence"
encodeValue = 13

# cipher = int(input("Enter the cipher number: "))
ciphAlphabet = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"
ciphAlphabet = (alphabet[encodeValue:] + alphabet[:encodeValue])
print(ciphAlphabet)

encodeDict = dict(zip(ciphAlphabet, alphabet))

print(encodeDict)

encodedTarget = ""

for ch in target.lower():
    if ch in encodeDict:
        encodedTarget += encodeDict[ch]
    else:
        encodedTarget += ch

print(len(encodedTarget))
print(encodedTarget)
