ls = [4, 1, 1, 2, 3, 4, 4, 12, 4, 12, 4, 5, 6, 8, 10, 11, 12]

ls_sort = sorted(ls)
print("the sorted list is {}".format(ls_sort))

outList = []

for i, item in enumerate(ls_sort):
    if ls_sort[i] == ls_sort[i - 1]:
        outList.append(ls_sort[i])

print("The list of multiple integers is {}".format(outList))

print("The set of multiple integers is {}".format(set(outList)))

# do without list
