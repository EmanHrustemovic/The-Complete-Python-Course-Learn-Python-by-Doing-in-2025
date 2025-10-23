def add_all(*args):
    return sum(args)

print(add_all(5,3,7,4))

def pretty_print(**kwargs):
    for k, v in kwargs.items():
        print(f'For {k} we have {v}.') #For name arguments

pretty_print(**{'username':'jose123','access_level':'admin'})

""" 
def add_all(a1,a2,a3,a4):
    return a1+a2+a3+a4

vals = (1,3,5,7)

print(add_all(1,3,5,7))
print(add_all(*vals))
"""