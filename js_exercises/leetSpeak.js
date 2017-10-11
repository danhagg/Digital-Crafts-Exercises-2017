
z = []

function leet(str1) {
  str = str1.toUpperCase()
  for (var i = 0; i < str.length; i++) {
    if (str[i] === 'A') {
      z.push('4')
    } else if (str[i] === 'E') {
      z.push('3')
    } else if (str[i] === 'G') {
      z.push('6')
    } else if (str[i] === 'I') {
      z.push('1')
    } else if (str[i] === 'O') {
      z.push('0')
    } else if (str[i] === 'S') {
      z.push('5')
    } else if (str[i] === 'T') {
      z.push('7')
    } else {
      z.push(str[i])
    }
  }console.log(z.join(''))
}
str = 'alex'

leet(str)
