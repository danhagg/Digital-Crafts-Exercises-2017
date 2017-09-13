# Given an list of numbers or strings, create a new list containing the same elements as the first list, except with any duplicate values removed. Print the list.

listOne = [4, 7, 8, 8, 'house', 'pants', 'house']
listTwo = set(listOne)
print(listTwo)
