var nums = [1, 2, 3, 4, 5]

var outList = []

for (let i = 0; i < nums.length; i++) {
  if (nums[i] % 2 === 0) {
    outList.push(nums[i])
  }
} console.log(outList)


console.log(
nums.map(function (n) {
  return n * 2
}))
