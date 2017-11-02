var express = require('express');
var app = express();

var animals = [
  { name: 'cats', favorite: true },
  { name: 'dogs', favorite: true },
  { name: 'tree frogs', favorite: true },
  { name: 'earth worms', favorite: false },
  { name: 'guinea pigs', favorite: true }
];

var lis = [];

app.get('/', function (request, response) {
  response.send('Hello World!');
});

// add meow at the url 'cats'
app.get('/cats', function (request, response) {
  response.send('MEOW');
});

// http://localhost:8000/hello?name=dan
// need to add ?name=dan to url
app.get('/hello', function (request, response) {
  var name = request.query.name || 'World';
  response.send('Hello ' + name);
});

// http://localhost:8000/greet?name=dan&age=41
app.get('/greet', function (request, response) {
  var name = request.query.name;
  var age = request.query.age;
  response.send('Hello ' + name + ', You were born in ' + (2017 - age));
});

// http://handlebarsjs.com/
// make new file views/app.js
app.set('view engine', 'hbs');

app.get('/hellohello', function (request, response) {
  var name = request.query.name || 'World';
  var context = {title: 'Hello', name: name};
  response.render('hello.hbs', context);
});

// http://localhost:8000/newGreet?age=41&name=dan
app.get('/newGreet', function (request, response) {
  var name = request.query.name;
  var age = request.query.age;
  var context = {age: age, name: name};
  response.render('newGreet.hbs', context);
});

function filterByTrue (animal) {
  if (animal.favorite === true) {
    return true;
  }
  return false;
}
var trueAnimals = animals.filter(filterByTrue);

app.get('/fav_animals', function (request, response) {
  var trueAnimals = {trueAnimals: animals.filter(filterByTrue)};
  response.render('animals.hbs', trueAnimals);
});

app.listen(8000, function () {
  console.log('Listening on port 8000');
});
