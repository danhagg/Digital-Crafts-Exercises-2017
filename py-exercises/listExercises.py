# The long way
listOne = [1, 2, 3, 4]
total = 0
for i in listOne:
    total = total + i
print(total)

# List comprehension

# The faster way
print(sum(listOne))

print(max(listOne))
print(min(listOne))

listOne = [1, 2, 3, 4]
evenList = []
for i in listOne:
    if i % 2 == 0:
        evenList.append(i)
print(evenList)

# list comprehension
evenList1 = [i for i in listOne if i % 2 == 0]
print(evenList1)

listTwo = [-3, -7, 0, 8, 4]
posList = [num for num in listTwo if num > 0]
print(posList)

factor = 3
outList = [j*factor for j in listTwo]
print(outList)

z=[]
x = [2, 4, 5]
y = [2, 3, 6]
for i in range(len(x)):
    z.append(x[i] * y[i])

c = [[0, 0],[0, 0]]
a = [[1, 3],[2, 4]]
b = [[5, 2],[1, 0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j] = a[i][j] + b[i][j]

for i in c:
    print(i)
