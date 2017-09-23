outList = [m*n for m in range(100, 1000) for n in range(100, 1000)]

outStrings = [str(x) for x in outList]

outStringsReversed = [j[::-1] for j in outStrings]

palList = [z for z in outStrings if z == z[::-1]]

outInts = [int(y) for y in palList]

print(max(outInts))
