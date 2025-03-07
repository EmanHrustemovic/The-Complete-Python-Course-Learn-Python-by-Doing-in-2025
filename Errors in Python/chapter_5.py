class Car :
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"<Car {self.make} {self.model}"



class Garage :
    def __init__(self):
        self.cars = []

    def __len__(self):
        return  len(self.cars)

    def add_car(self,car):
        if not  isinstance(car, Car) :
            raise  TypeError(f"Tried to add a  {car.__class__.__name__} to the garage , but you can onyl add Car objects")
        self.cars.append(car)

ford = Garage()
fiesta = Car('Ford','Fiesta')

'''
print(len(ford))
car = Car('Ford','Fiesta')
ford.add_car(car)
'''
ford.add_car(fiesta)
try:
    ford.add_car('Fiesta')
except TypeError :
    print("Your car is not a Car")
except ValueError :
    print("Something weird happened")
finally:
    print(f"The Garage now have a length {len(ford)} cars !!")

    