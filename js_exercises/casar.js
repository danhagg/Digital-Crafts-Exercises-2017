target = "Encode this sentence"
cipher = 13

spacer = " "
alphabet = list("abcdefghijklmnopqrstuvwxyz")
ciphAlphabet = alphabet[cipher:] + alphabet[:cipher]

alphabet.extend(spacer)
ciphAlphabet.extend(spacer)

dictCipher = dict(zip(ciphAlphabet, alphabet))

print(dictCipher)

cipherOut = ""
for ch in target.lower():
    cipherOut += dictCipher[ch]

print(cipherOut)
