#IF STATEMENTS IN PYTHON

friend = "Rolf"
user_name = input("Please enter your name : ")

if (user_name == friend) :
    print("Hello , friend !")
else :   
    print("Hello stranger ! ")

print(bool(0))

friends =["Rolf","Bob","Anne"]
family = ["Jen","Charlie"]

user = input("Please enter your name : ")

if(user in friends) : 
    print("You are my friend !")
elif(user in family) :
    print("You are my family member !")
else :
    print("I don't know you man !")

#WHILE LOOP 

is_learning = True

while(is_learning) : 
    print("You are learning ! ")
    #is_learning = False
    user_input = input("Are you still learning ? : ")
    is_learning = user_input == "yes"

user_input = input("Do you want to start program ? : ")

while (user_input=="yes") : 
    print("Programm is running !")
    user_input = input("Do you want to run program ? (yes/no) : ")

print("We stopped running.")

#FOR LOOP 

friends =["Rolf","Bob","Anne"]

for friend in friends : 
    print(friend)

elements = [0,1,2,3,4,5,6,7,8,9]

for element in elements : 
    print(element)

for i in range(10) : 
    print(i)

students = [
    {"name" : "Anne","grade" : 70},
    {"name" : "Bob","grade" : 75},
    {"name" : "Rolf","grade" : 55}
]

for student in students : 
    name = student["name"]
    grade = student["grade"]

    print(f"{name} : has a grade : {grade}")

#DESTRUCTIONS

currencies = (0.8 , 1.2)
usd , eur = currencies

mates = [("Rolf",25),("Anne",37),("Charlie",31),("Bob",22)]

for name,age in mates : 
    print(f"{name} is {age} years old ")

friends_age = {"Rolf": 25 , "Anne" : 37 ,"Charlie" : 31 , "Bob" : 22}

for name in friends_age :
    print(name)

for age in friends_age.values():
    print(age)

for name,age in friends_age.values() :
    print(name,age)

for name,age in friends_age.items() :
    print(f"{name} has : ,{age} age ")

#BREAK AND CONTINUES

cars = ["ok","ok","ok","bad","ok","ok"]

for car in cars :
    if car == "bad" :
        print("Found faulty car ! Skipping ...")
        continue
    print(f"This car is : {car} .")
    print("Shipping new car to our customer")

#FINDING PRIME NUMBER : 

is_prime = True

for n in range(2,10) :
    for i in range(2,n) : 
        if(n%i==0) :
            print(f"{n} equals {i} * {n//i}")
            break;
    else : 
        print(f"{n} is prime number ")

##LIST SLICING

team = ["Rolf","Charlie","Anna","Bob","Jen"]
print(team[2:4])
print(team[1:])
print(team[:2])
print(team[-3])

#LIST COMPREHENSION

numbers = [0,1,2,3,4]
doubled_numbers =[]

#FIRST SOLUTION ( without LIST COMPREHENSION) : 

for i in numbers : 
    doubled_numbers.append(i*2)
print(doubled_numbers)

#SECOND SOLUTION ( with LIST COMPREHENSION) : 

doubled_numbers = [number*2 for number in numbers]
print(doubled_numbers)

friends_ages = [22,31,35,37]
age_descriptions = [f"My friend is {age} old ." for age in friends_ages]
print(age_descriptions)

names = ["Rolf", "Bob", "Jane"]

lower = [name.lower() for name in names]
print(lower)

friend = input("Please enter your name : ")
friends_list = ["Rolf","Bob","Jen","Anne","Charlie"]
friends_lower = [name.lower() for name in friends_list]

if(friend.lower() in friends_lower) : 
    print(f"{friend} is my friend .")
else :
    print("We don't know each other !")

#CONDITIONAL COMPREHENSION
ages = [22,35,27,21,20]
odds = [age for age in ages if age % 2 != 0]
print(odds)

#FIRST METHOD 
friends = ["Rolf","ruth","charlie","Jen"]
guests = ["jose" , "Bob", "Rolf", "Charlie","michael"]

friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])

print(friends_lower.intersection(guests_lower))

# SECOND METOD 
friends_lower = [f.lower() for f in friends]

presnet_friends = [
    name.title() 
    for name in guests 
    if name.lower() in friends_lower
]
print(presnet_friends)

# SET AND DICTIONARIES COMPREHENSION
friends_lower = {n.lower() for n in friends}
guests_lower = {g.lower() for g in guests}

presnet_friends = {name.title() for name in friends_lower.intersection(guests_lower)}
print(presnet_friends)

friends = ["Bob", "Rolf","Jen","Anne"]
time_since_seen = [3,7,15,11]

long_timers = {
    friends[i] : time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}
print(long_timers)

#ZIP FUNCTION 
friend_names = dict(zip(friends,time_since_seen)) # SHORTER WAY OF COMPREHENSION
print(friend_names)

#ENUMERATE FUNCTION
family_guy = ["Peter","Louis","Meg"]

for counter , i in enumerate(family_guy) : 
    print(counter)
    print(i)

print(list(enumerate(family_guy)))
print(dict(enumerate(family_guy)))


# FUNCTIONS 

def greet() :
    name = input("Please enter your name : ")
    print(f"Hello , {name}")

print(greet())


cars = [
    {"make" : "Ford","model": "Fiesta","mileage" : 2300,"fuel_consumed" : 460},
    {"make" : "Ford","model": "Focus","mileage" : 1700,"fuel_consumed" : 350},
    {"make" : "Mazda","model": "MX-5","mileage" : 4900,"fuel_consumed" : 900},
    {"make" : "Mini","model": "Cooper","mileage" : 3100,"fuel_consumed" : 235}
]

def calculate_mpg(car_to_calculate) : 

    mpg = round(car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"],2)
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon .")

calculate_mpg(cars[0])
calculate_mpg(cars[1])
calculate_mpg(cars[2])

for car in cars :
    calculate_mpg(car)

## FUNCTIONS AND RETURN VALUE 

cars = [
    {"make" : "Ford","model": "Fiesta","mileage" : 2300,"fuel_consumed" : 460},
    {"make" : "Ford","model": "Focus","mileage" : 1700,"fuel_consumed" : 350},
    {"make" : "Mazda","model": "MX-5","mileage" : 4900,"fuel_consumed" : 900},
    {"make" : "Mini","model": "Cooper","mileage" : 3100,"fuel_consumed" : 235}
]

def calculate_mpg(car) : 

    mpg = round(car["mileage"] / car["fuel_consumed"],2)
    return mpg


def car_name(car) :
    name = f"{car['make']} {car['model']}"
    return name


def print_car_intro(car): 
    name = car_name(car)
    mpg = calculate_mpg(car)

    print(f"{name},does {mpg} miles per gallons")


for car in cars :
    print_car_intro(car)

def divide(x, y):
    if y==0:
        return "You can't divide numbers with 0 !!"
    else:
        return x/y

print(divide(10,2))

#DEFAULT VALUES FOR PARAMETERS

def add(x,y=3):
    total = x + y
    return total
print(add(x=5 , y=7))

print(1,2,3,4,5, sep='-')

#LAMBDA FUNCTION 

divide = lambda x,y : x/y
print(divide(10,2))

def average(sequence):
    return sum(sequence)/len(sequence) ##WWITHOUT LAMBDA 

students = [
    {"name":"Rolf","grade":(75,90,95,100)},
    {"name":"Bob","grade":(56,78,80,90)},
    {"name":"Jen","grade":(98,90,95,99)},
    {"name":"Anne","grade":(100,100,95,100)},
]

for student in students :
    print(average(student["grade"]))

#First-class Functions

average = lambda seq : sum(seq) / len(seq)
total = lambda seq : sum(seq)
top = lambda seq : max(seq)


operations = {
    "average" : average,
    "total": total,
    "top" : top
}

students = [
    {"name":"Rolf","grade":(75,90,95,100)},
    {"name":"Bob","grade":(56,78,80,90)},
    {"name":"Jen","grade":(98,90,95,99)},
    {"name":"Anne","grade":(100,100,95,100)},
]

for student in students : 
    name = student["name"]
    grade = student["grade"]

    print(f"Student : {name}")
    operation = input("Enter 'average' , 'total' or 'top' : ")

    operation_functions = operations[operation]
    print(operation_functions(grade))
    