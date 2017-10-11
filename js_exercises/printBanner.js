
starLineA = []
starLineC = []

function printBox (width, height) {
  /* make a list of * for full width */
  for (var i = 0; i < width; i++) {
    starLineA.push('*')
    /*join the list*/
  } console.log(starLineA.join(''))

  /* make a list '*' + spaces + '*' */
  starLineC.push('*')
  var b = ' '.repeat(width - 2);
  starLineC.push(b)
  starLineC.push('*')

/*print to console height-2 of these lists... joined*/
  for (var i = 0; i < height - 2; i++) {
    console.log(starLineC.join(''))
  } console.log(starLineA.join(''))
}
printBox(10, 4)
