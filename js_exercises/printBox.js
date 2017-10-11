starLineA = []
starLineC = []

function printBox (num1, num2) {
  for (var i = 0; i < num1; i++) {
    starLineA.push('*')
  } console.log(starLineA.join(''))
  starLineC.push('*')
  var b = ' '.repeat(num1 - 2);
  starLineC.push(b)
  starLineC.push('*')

  for (var i = 0; i < num2 - 2; i++) {
    console.log(starLineC.join(''))
  } console.log(starLineA.join(''))
}
printBox(10, 4)
