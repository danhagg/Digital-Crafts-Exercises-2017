ls = [1,2]
evenNumList = []
for i in range(1,1000000):
    ls.append(ls[-1] + ls[-2])
    if ls[-1] >= 4000000:
        break
newList = ls[0:-1]

for j in newList:
    if j % 2 == 0:
        evenNumList.append(j)

print(ls)
print(newList)
print(evenNumList)
print(sum(evenNumList))
