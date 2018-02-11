var animals = [
  { name: 'cats', favorite: true },
  { name: 'dogs', favorite: true },
  { name: 'tree frogs', favorite: true },
  { name: 'earth worms', favorite: false },
  { name: 'guinea pigs', favorite: true }
];

function filterByTrue (animal) {
  if (animal.favorite === true) {
    return true;
  }
  return false;
}

var trueAnimals = animals.filter(filterByTrue);
console.log(trueAnimals);

var cat = { name: 'cats', favorite: true };
console.log(cat.name);

for (let i = 0; i < animals.length; i++) {
  console.log(animals[i].name);
}
