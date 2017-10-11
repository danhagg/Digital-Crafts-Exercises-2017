starLine = [];
function printSq (num) {
  for (var i = 0; i < num; i++) {
    starLine.push('*')
    console.log(starLine)
  } for (var i = 0; i < num; i++) {
    console.log(starLine.join(''))
  }
}

printSq(5)
