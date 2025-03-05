my_student = {
    'name' : 'Rolf Smith',
    'grades' : [70,88,90,99]
}
def average_grade(student):
    avg = sum(my_student['grades']) / len(my_student['grades'])
    return  avg

print((average_grade(my_student)))

class Student :

    def __init__(self,new_name,new_grade):
        self.new_name = new_name
        self.new_grade = new_grade

    def average(self):
        return  sum(self.new_grade) / len(self.new_grade)

student_one = Student('Rolf Smith',[70,88,90,99])

print(student_one.new_name)

print(student_one.average())

class Movie():
    def __init__(self, name, year):
        self.name = name
        self.year = year


movie = Movie('Matrix',1994)
print(movie.name)
print(movie.year)


class Friend():
    def __init__(self,name):
        self.name = name

squad = ['Bob', 'Alex', 'John', 'Dimitri']
print(squad.__class__)

class Garage():
    def __init__(self):
        self.cars = []

    def __len__(self): ## Dunder method for length of class
        return len(self.cars)

    def __getitem__(self, item): ##Dunder method for indexing
        return self.cars [item]

    def __repr__(self): ##Dunder raper representing the object
        return  f"Garage {self.cars}"

    def __str__(self): ## Dunder string method
        return f"Garage with {len(self)} cars ."


ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(len(ford))
print(ford)

for car in ford :
    print(car)

#Inheritance In Python

class Students :
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent(Students):
    def __init__(self, name, school, salary):
        super().__init__(name, school) ##Inheritance
        self.salary = salary

    @property
    def weekly_salary(self):
        return  self.salary * 37.50


rolf = WorkingStudent('Rolf','MIT',15.50)
print(rolf.weekly_salary)

ben = Students('Ben','MIT')
ben.marks.append(70)
ben.marks.append(100)
print(ben.average())

'''
print(rolf.salary)
rolf.marks.append(60)
rolf.marks.append(100)
print(rolf.average())
'''
'''
print(rolf.weekly_salary)
print(rolf.weekly_salary())

anna = Students('Anna','Oxford')
print(anna.school)

'''

class Foo :
    @classmethod
    def hi(cls) :
        print(cls.__name__)

my_object = Foo()
my_object.hi()

class Bar :
    @staticmethod
    def hi():
        print("Hello , I don't take parameters !")

bar = Bar()
bar.hi()

class FixedFloat :
    def __init__(self,amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount : .2f}>'

    #@staticmethod
    @classmethod
    def from_sum(cls,value1,value2):
        return  cls(value1+value2)

new_number = FixedFloat.from_sum(0.789,19.575)
print(new_number)

class Euro(FixedFloat) :
    def __init__(self,amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return  f'<Euro {self.symbol}{self.amount : .2f}'

money = Euro(18.786)
print(money)