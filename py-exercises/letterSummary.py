phrase = "banana"

def letter_count(phrase):
    dictWord = {}
    phraseList = list(phrase) # make a list of all letters
    dictWord = {letter: phraseList.count(letter) for letter in phraseList} # make the dictCipher
    return dictWord

print(letter_count(phrase))
