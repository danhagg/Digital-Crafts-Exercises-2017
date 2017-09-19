
target = "Encode this sentence"
cipher = 13

# cipher = int(input("Enter the cipher number: "))
spacer = " "
alphabet = list("abcdefghijklmnopqrstuvwxyz")
print(alphabet)
ciphAlphabet = alphabet[cipher:] + alphabet[:cipher]
print(ciphAlphabet)

#without list, straight to dictCipher
#dict(zip() ch in strings

dictCipher = dict(zip(ciphAlphabet, alphabet))

print(dictCipher)

cipherOut = ""
# for ch in target.lower():
#     if #ch in dict

    # cipherOut += dictCipher[ch]
    # else += ch

print(cipherOut)

# outString = ""
# for i in range(len(target)):
#     outString.join()
