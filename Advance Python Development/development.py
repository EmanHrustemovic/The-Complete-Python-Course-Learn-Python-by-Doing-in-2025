'''Mutability in Python'''

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