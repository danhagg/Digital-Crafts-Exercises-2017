var a = [1, 2, 3]

// The reduce() method applies a function against an accumulator and each element in the array (from left to right) to reduce it to a single value.

var b = a.reduce(function (sum, value) {
  return sum + value
})

console.log(b)
