from collections import Counter
import matplotlib.pyplot as plt

phrase = "To be or not to be"
wordDict = {}
def word_count(phrase):
    global wordDict
    phrase = [char if char.isalnum() else ' ' for char in phrase.lower()]
    words = ''.join(phrase).split()
    wordDict = {word: words.count(word) for word in words}
    return wordDict

word_count(phrase)

# def  letter_hist3(word):
#     tally = {}
#     for character in word:
#         if character in tally:
#             tally[character] += 1
#         else:
#             tally[character] = 1
# print(tally)
mostCommon = dict(Counter(wordDict).most_common(2))

print(mostCommon)

plt.bar(range(len(wordDict)), wordDict.values(), align='center')
plt.xticks(range(len(wordDict)), wordDict.keys())

plt.show()
