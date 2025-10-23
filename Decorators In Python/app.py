import functools

user = {'username' : 'jose123', 'access_level' : 'user'}

def third_level(access_level):
    def my_decorator(func):
        @functools.wraps(func)
        def secure_func(panel):
            if user.get('access_level') == access_level:
                return func(panel)
        return secure_func
    return my_decorator

@third_level('user')
def my_function(panel):
    """
    Allows us to retrieve the password for admin panel.
    """
    return f'Password for {panel}  panel is 1234.'

#print(my_function('movies'))
print(my_function.__name__)
#print(my_function.__doc__) using this to show comments/documentation we made

print(my_function('movies'))