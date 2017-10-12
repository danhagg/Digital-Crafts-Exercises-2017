var str = 'banana'
var histogram = {}

for (var i = 0, len = str.length; i < len; i++) {
  var letter = str[i]
  histogram[letter] = (histogram[letter] || 0) + 1
}

console.log(histogram)
