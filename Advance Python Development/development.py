'''Mutability in Python'''
from logging import DEBUG

friends_last_seen = {
    'Rolf' : 31 ,
    'Jenn' : 1 ,
    'Anne' : 7
}

print(id(friends_last_seen))

friends_last_seen['Rolf'] = 0
print(id(friends_last_seen))

my_int = 5
print(id(my_int))

my_int=my_int+1
print(id(my_int))

friends = ['Rolf','Jose']
print(id(friends))

friends.append('Jen')
print(id(friends))

'''
integers
float
strings          (ALL IMMUTABLE)
tuples  
'''

'''Argument mutability in Python'''

def see_friend(friends,name) :

    friends[name] = 0

see_friend(friends_last_seen,'Rolf')
print((friends_last_seen['Rolf']))

age = 20

def increase_age(current_age):
    current_age = current_age+1

id(age)
increase_age(age)
id(age)

'''Default values for parameters'''

accounts = {
    'checking' : 1958.00,
    'savings' : 3695.50
}

def add_balance(amount : float , name : str) :
    accounts[name] += amount
    return accounts[name]


add_balance(500.00,'savings')
print(accounts['savings'])

'''Mutable default arguments (bad idea)'''

def create_account(name : str ,holder : str , account_holders : list = []) :
    account_holders.append(holder)

    return {
        'name' : name,
        'holder' : holder,
        'account_holders' : account_holders
    }
a1 = create_account('checking','Rolf')
a2 = create_account('saving','Jen')

print(a2)

'''Argument unpacking in Python'''

accounts = {
    'checking' : 1958.00,
    'savings' : 3695.50
}

def add_balance(amount : float , name : str) :
    accounts[name] =+ amount
    return accounts[name]

transactions = [
    (-180.67,'checking'),
    (-220.00,'checking'),
    (220.00,'saving'),
    (-17.50,'checking'),
    (-23.90,'checking'),
    (-220.00,'checking'),
    (-13.00,'checking'),
    (-600.50,'checking'),
    (600.50,'saving'),
]

for t in transactions :
    add_balance(*t) #unpack iterable into variables
    add_balance(amount=t[0] , name=t[1])


''' 1. Counter'''

from collections import Counter

device_temperatures =[13.5,14.0,14.0,14.5,14.5,14.5,15.0,16.0]

temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.0])

''' 2. DefaultDict'''

from collections import defaultdict

coworkers = [('Rolf','MIT'),('Jen','Oxford'),('Rolf','Cambridge'),
             ('Charlie','Manchester')]

alma_maters = defaultdict(list)

for coworker , place in coworkers:
    alma_maters[coworker].append(place)

print(alma_maters['Rolf'])
print(alma_maters['Anne'])

''' 3. OrderedDict'''

from  collections import OrderedDict

o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 12
o['Jenn'] = 3

print(o)

''' 3. NamedTuple'''

from collections import namedtuple

account = ('checking' , 1850.90)

Account = namedtuple('Account', ['name', 'balance'])

account = Account('checking' , 1850.90)
print(account.name)

''' 4. Deque'''

from collections import deque

friends = deque(('Rolf','Charlie','Jenn','Anna'))

friends.append('Jose')
friends.appendleft('Antony')
friends.pop()
friends.popleft()
print(friends)

''' Dates and time in Python '''

from datetime import datetime, timezone, timedelta

print(datetime.now())
print(datetime.now(timezone.utc)) #utc - stands for "standard" zone

today = datetime.now()
tomorrow = today - timedelta(days=1)

print(today)
print(tomorrow)

print(today.strftime('%d-%m-%Y %H:%M:%S')) #formating the time and date in format we want

user_date = input('Enter the date in YYYY-mm-dd format : ')
user_date =datetime.strptime(user_date,'%Y-%m-%d')
print("User date is : " , user_date)

'''Timing code with Python'''

import time

def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)


def powers(limit):
    return [x**2 for x in range(limit)]
    #print(powers(5))

measure_runtime(lambda:powers(500000))

import timeit

print(timeit.timeit("[x**2 for x in range(10)]"))

'''Regex in Python'''

import  re

email = 'jose@tecladocode.com'
expression = '[a-z]+'

matches = re.findall(expression,email)
print(matches)

name = matches[0]
domain = f'{matches[1]}.{matches[2]}'

print(name)
print(domain)

expression = '[a-z/.]+'
name = matches[1]
print(name)

price = 'Price : $189.50'
expression = 'Price : \$([0-9]*\.[0-9]*)'

matches = re.search(expression,price)
print(matches.group(0))
print(matches.group(1))

'''Introduction to logging in Python'''

import logging
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s' , level=logging.DEBUG)
#logging.basicConfig(level = logging.DEBUG)##OR DEBUGGING

logger = logging.getLogger('test_logger')

logger.info('This will not show up.')
logger.warning('This will.')
logger.debug('This is a debug message.')
logger.critical('This is critical !!')

'''Higher-order functions in Python'''

def greet():
    print("Hello")

def before_and_after(func) :
    print("Before ....")
    func()
    print("After ..")

# before_and_after(5) - error since must be a function
before_and_after(greet)

movies = [
    {"name" : "The Matrix" , "director" : "Wachowski"},
    {"name" : "A beautiful day in the neighborhood", "director" : "Heller"},
    {"name" : "The Irishman" , "director" : "Scorceses"},
    {"name" : "Klaus" , "director" : "Pablos"},
    {"name" : "1917" , "director" : "Mendes"}
]

def find_movie(expected,finder):
    for movie in movies:
        # print(finder(movie))
        found = []
        if finder(movie) == expected:
            found.append(movie)

find_by = input("What property we are searching by? :")
looking_for = input("What are you looking for ? : ")

movie = find_movie(looking_for, lambda movie : movie[find_by])
print(movie or "No movie found.")