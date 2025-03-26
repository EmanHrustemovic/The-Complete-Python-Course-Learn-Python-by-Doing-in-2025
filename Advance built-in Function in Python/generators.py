'''GENERATOR FUNCTIONS'''

def hundred_numbers():
    nums = []
    i = 0
    while i<100:
        yield i
        ##nums.append(i)
        i+=1
        ##return  nums

g = hundred_numbers()
print(next(g))
print(next(g))
print(list(g))
#print(hundred_numbers())

'''RANGE Example'''

my_range_obj=range(10)
print(my_range_obj)


'''Python generator classes and iterators'''

class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100 :
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self

my_gen = FirstHundredGenerator()
next(my_gen)
next(my_gen)


'''Iterables in Python'''

''' 
print(sum(FirstHundredGenerator()))

for i in FirstHundredGenerator() :
    print(i)
'''

class AnotherIterable:
    def __init__(self):
        self.cars=['Fiesta','Focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

for car in AnotherIterable():
    print(car)

my_numbers = [x for x in [1,2,3,4,5]]
my_numbers_gen =(x for x in [1,2,3,4,5])

print(next(my_numbers_gen))


class FirstFiveIterator:
    def __init__(self):
        self.numbers = [1,2,3,4,5]
        self.i = 0

    def __next__(self):
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i +=1
            return current
        else:
            raise  StopIteration()


FirstFiveIterator()

'''The filter() function in Python'''

def starts_with_r(friend):
    return  friend.startswith('R')

our_friends = ['Rolf','Jose','Randy','Anna','Marry']
start_with_r = filter(starts_with_r,our_friends) # First argument is function that return True/False
                                                 #Second argument is iterable
print(next(start_with_r))
print(next(start_with_r))


another_start_with_r = (o for o in our_friends if o.startswith('R')) #GENERATOR COMPREHENSION WAY OF FUNCTION


'''The map() function in Python'''

friends_lower = map(lambda x :x.lower(), our_friends) # using map function
friends_small =(our_friends.lower() for our in our_friends )
print(next(friends_lower))
print(friends_small)


class User :
    def __init__(self,username,password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls,data):
        return  cls(data['username'],data['password'])

users = [
    {'username' : 'Rolf' , 'password' : '123'},
    {'username' : 'edward@gmail.com' , 'password' : 'youaretoo'}
]

#users = [User.from_dict(user) for user in users]
#users = map(User.from_dict(),users)

'''any() and all() in Python'''

friends = [
    {
        'name' : 'Rolf' ,
        'location' : 'London'
    },
    {
        'name' : 'Anne' ,
        'location' : 'Moscow'
    },
    {
        'name' : 'Charlie' ,
        'location' : 'Sarajevo'
    },
    {
        'name' : 'Jose' ,
        'location' : 'Madrid'
    },
]
your_location = input("Where are you now ? : ")
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby):
    print("You are not alone !!!")

print(all([0,1,2,3,4,5]))

#print(friends_nearby)
