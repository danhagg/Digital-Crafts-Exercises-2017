z = []

function longV(str) {
  for (var i = 0; i < str.length; i++) {
    if (str[i] === str[i-1]) {
      z.push(str[i].repeat(5))
    }
    else {
      z.push(str[i])
    }
  } console.log(z.join(''))
}

longV('cheese')
