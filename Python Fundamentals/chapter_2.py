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
