class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def printInfo(self):
        print('The car\'s make, model and year are {}, {}, and {}, repectively!'.format(self.make, self.model, self.year))

car = Vehicle('Nissan', 'Leaf', '2015')

car.printInfo()
