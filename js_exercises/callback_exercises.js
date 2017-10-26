function add(x, y, callback) {
var result = x + y;
callback(result);
}

add(1,2, function(result) {
  console.log(result);
});


function subtract(a, b, callback) {
var result = a - b;
callback(result);
}

subtract(1,2, function(result) {
  console.log(result);
});



function greeting(person, callback) {
var result = console.log('hola ' + person)
callback(result);
}
greeting('Dan', function(person) {
  console.log(person);
});


var numbers = [1,2,3];

function mult (x, y, callback) {
  setTimeout(function () {
    var result = x * y;
    callback(result);
  });
}
mult(3, 5, function (result) { console.log(result); });


var numbers = [1,2,3,4, 5,6]

function product (numbers, callback) {
  setTimeout(function () {
    var result = numbers.reduce(function(a, b) {
      return a * b;
    }, 1);
    callback(result);
  });
}
product(numbers, function (result) { console.log('The DELAYED REDUCE is ' + result); });





var numbers1 = [5]
function product1 (numbers1, callback) {
  var result = numbers1.reduce(function(a, b) {
    return a * b;
  });
  callback(result);
};

product1(numbers1, function (result) {
  console.log('This is the REDUCE result ' + result);
})
