# vector multiplication
z=[]
x = [2, 4, 5]
y = [2, 3, 6]
for i in range(len(x)):
    z.append(x[i] * y[i])   
print(z)

# list comprehension
vec = [x[i]*y[i] for i in range(len(x))]
print(vec)

# enumerate
answer = []
for i, num1 in enumerate(x):
    answer.append(num1* y[i])
print(answer)





# This is not my work but am impressed with it
result = [[0, 0],[0, 0]]
X = [[1, 3],[2, 4]]
Y = [[5, 2],[1, 0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)

# list comprehension
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
for r in result:
   print(r)
