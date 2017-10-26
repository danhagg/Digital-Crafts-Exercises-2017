function Person (name, email, phone) {
  this.name = name
  this.email = email
  this.phone = phone
}

Person.prototype.greet = function (other) {
  console.log('Hello ' + other.name + ', I am ' + this.name + '!')
}

var sonny = new Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
var jordan = new Person('Jordan', 'jordan@hotmail.com', '555-555-5555')

sonny.greet(jordan)
jordan.greet(sonny)

console.log(sonny.email, sonny.phone)
console.log(jordan.email, jordan.phone)
