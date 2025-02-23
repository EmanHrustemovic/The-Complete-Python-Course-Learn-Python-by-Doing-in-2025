##Numbers in Python 

age = 35 #integer
PI = 3.14159 #float

math_operation = 1 + 3 * 4 / 2 - 2
print(math_operation)

floating_division = 8 / 3
print(floating_division)

integer_devision = 8 // 3
print(integer_devision)

# Calculating the remainder of division

num = 13 // 5
print(num)

#remainder = 13 % 5
#print(remainder)

x = 37
remainder = x % 2 
print(remainder)

#STRINGS 

my_string = "Hello , world"
print(my_string)

string_with_quotes = "Hello it's me "
another_with_quotes = 'He said  "You are amazing!!" yesterday'
print(string_with_quotes)
print(another_with_quotes)

multiline = """Hello world ,

My name is Eman . This is Python course
"""
print(multiline)

name = "Eman"
greeting = "Hello"
print(greeting, name)

age = 35
#print("You are " + age  +"years old")

##String Formating

age = 34
print(f"You are {age}")

name = "Jose"
greeting = f"How are you, {name} ?"
print(greeting)

name = "Jose"
final_greeting="How are you, {}?"
jose_greeting = final_greeting.format(name)
print(jose_greeting)

bob_greeting=final_greeting.format("Bob")
print(bob_greeting)

eman_greeting=final_greeting.format("Eman")
print(eman_greeting)

## Getting user input 
my_name = "Eman"
your_name = input("Please enter your name : ")
print(f"Hello {your_name} . My name is {my_name}")

age = int(input("Please enter your age : "))
print(f"You have lived {age*12} months")

## Booleans and comparations

thruthy = True
falsy = False

age = 20
is_over_age = age > 18
print(is_over_age)

is_under_age = age < 19
print(is_under_age)

is_twenty = age == 20
print(is_twenty)

our_number = 5
user_number = int(input("Guess my number : "))

mathed_number = our_number == user_number
print(f"You got it right : {mathed_number} .")

#AND & OR  
#AND  - if both are true 
#OR - if either of them is true

age = int(input("Please enter your age : "))
result = age > 18 and age < 65 #ture AND true
print(result)

my_age = int(input("Please enter my age : "))
result = my_age > 18 or age < 65 #
print(result)

bool(0)
bool(13) 

bool(" ")
bool("Hello")

bool([])
bool([1,2,3])

default_age = 30
age = 0

user_age = age or default_age
print(user_age)

default_greeting = "There ,"
name = input("Please enter your name  : (optional) ")

user_name = name or default_greeting
print(f"Hello , {user_name}")

### LISTS IN PYTHON 

friends = ["Rolf","Bob", "Anne"]
print(friends[0])
print(len(friends)) # len - calculate the length of list
friends.append("Eman")
friends.remove("Rolf")

friends1 = [["Rolf",24],
["Bob",35],
["Anne",18]]
print(friends1[0][0])

#TUPLES 
short_tuple = "Rolf" , "Bob"
a_bit_clear = ("Rolf","Bob") #YOU DON'T ADD THROUGH APPEND METHOD
new_tuple = a_bit_clear + ("Jan",) # ADDING IN THE TUPLES
print(new_tuple) 

#SETS - don't hold order and don't contain duplicates

art = {"Eman","Davide", "Jen"}
science = {"Jen","Charlie"}
art.add("Jen")
print(art)
art.remove("Jen")
print(art)

art_not_science = art.difference(science) # pronalazi elemente koji nisu u science tj razliku elemenata
print(art_not_science)

not_in_both = art.symmetric_difference(science)
print(not_in_both)

art_and_science = art.intersection(science)
print(art_and_science)

all_friends = art.union(science)
print(all_friends)

#DICTIONARIES 

my_dict = {"Rolf":24,"Adam" : 30,"Anne":27}
print(my_dict["Rolf"])
my_dict["Bob"] = 15
my_dict["Rolf"] = 25
print(my_dict)

friends = (
    {"name" : "John Smith" , "age" : 70},
    {"name" : "John Berets" , "age" : 40},
    {"name" : "John Will" , "age" : 70}
)
print(friends[0]["name"])

squad = [("Rolf" , 24),("Kuki",7),("Ben",45)]
new_dict =dict(squad)
print(new_dict)

#SUM AND LENGTH
grades = [70,80,90,100]
total = sum(grades)
print(total)

lenght=len(grades)
print(grades)

avg = round((total/lenght),2)
print(avg)

#JOINING THE LIST 
friends = ["Alex","Ben","Max"]
comma_separated = " , ".join(friends)
print(comma_separated)