
nonPrimes = []
n = 600851475143
j = list(range(2, n+1))
nonPrimes = [i for i in j if any (i % j in range(2, i-1) == 0])

fullList = list(range(1, n+1))

allPrimes = set(fullList) - set(nonPrimes)

print(sum(allPrimes))
