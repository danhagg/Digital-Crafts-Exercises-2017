/*
Write a function positiveNumbers which is given an array of numbers and returns a new array containing only the positive numbers within the given array.
*/
x = []

function positiveNumbers(nums) {
  for (var i = 0; i < nums.length; i++) {
    if (Math.sign(nums[i]) === 1) {
      x.push(nums[i])
    }
    else if (Math.sign(nums[i]) === 0) {
      x.push(nums[i])
    }
  } console.log(x)
}

positiveNumbers([1, -3, 5, -3, 0])
