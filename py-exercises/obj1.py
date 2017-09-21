class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.counter = 0
        self.greets = []

    def greet(self, otherPerson):
        print('Hello {}, I am {}!'.format(otherPerson.name, self.name))
        self.counter += 1
        print("{0} has {1} meeting".format(self.name, self.counter))
        if otherPerson not in self.greets:
            self.greets.append(otherPerson)
            self.uniqueGreetings()

    def uniqueGreetings(self):
        print("{0} has met {1} people".format(self.name, len(self.greets)))

    def printContactInfo(self):
        print("{0}'s phone number is {1} and email is {2}". format(self.name, self.phone, self.email))

    def addFriend(self, otherPerson):
        self.friends.append(otherPerson)
        print("{0} has {1} friends".format(self.name, len(self.friends)))

    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

sonny = Person('Sonny', 'sonny@hotmail.com', '495-586-3456')
jordan = Person('Jordan', 'jordan@hotmail.com', '555-555-5555')

jordan.greet(sonny)
jordan.addFriend(sonny)

print(jordan)
