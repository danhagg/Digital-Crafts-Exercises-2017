var ls = [4, 1, 1, 2, 3, 4, 4, 12, 4, 12, 4, 5, 6, 8, 10, 11, 12]

var lsSort = ls.sort()

var outList = []

for (let i = 0; i < lsSort.length; i++) {
  if (lsSort[i] === lsSort[i - 1]) {
    outList.push(lsSort[i])
  }
}

console.log(outList)

var setList = new Set(outList)

console.log(setList)
