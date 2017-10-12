var cities = [{
    name: 'Los Angeles',
    temperature: 60.0
  },
  {
    name: 'Atlanta',
    temperature: 52.0
  },
  {
    name: 'Detroit',
    temperature: 48.0
  },
  {
    name: 'New York',
    temperature: 80.0
  }
]



for (let i = 0; i < cities.length; i++) {
  if (cities[i].temperature < 70) {
    console.log(cities[i].temperature)
  }
}


/*
for (var attribute in person) {
  var value = person[attribute];
  console.log(`${attribute}: ${value}`);
}
*/
