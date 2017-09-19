from collections import Counter
import matplotlib.pyplot as plt

name = input("Please enter a filename: ")+'.txt'

with open(name, 'w') as f:
    contents = f.write(input("Pleae enter some text: "))
    print(contents)

with open(name, 'r') as f:
    phrase = f.read(contents)

def letter_count(phrase):
    global dictWord
    phraseList = list(phrase) # make a list of all letters
    dictWord = {letter: phraseList.count(letter) for letter in phraseList} # make the dictCipher
    return dictWord

print(letter_count(phrase))

wordDict = {}
def word_count(phrase):
    global wordDict
    phrase = [char if char.isalnum() else ' ' for char in phrase.lower()]
    words = ''.join(phrase).split()
    wordDict = {word: words.count(word) for word in words}
    return wordDict

word_count(phrase)

mostCommon = dict(Counter(wordDict).most_common(2))

print(mostCommon)

plt.bar(range(len(wordDict)), wordDict.values(), align='center')
plt.xticks(range(len(wordDict)), wordDict.keys())

plt.show()

plt.bar(range(len(dictWord)), dictWord.values(), align='center')
plt.xticks(range(len(dictWord)), dictWord.keys())

plt.show()
