a = [1, 2, 2, 3, 3, 3, 3, 4, 1, 2, 7, 99, 11, 909]
b = [99, 11, 3]

A = set(a)
B =set(b)


C = A.difference(B)
print(C)

D = A.intersection(B)
print(D)

print(D.issubset(A))

G = A -B
print("A is", A)
print("B is", B)
print("A - B is ", G)
B.add(67)
H = A ^ B
print(H)

M = A | B
print(M)