
def find_in(iterable, finder, excepted):
    for i in iterable:
        if finder(i) == excepted:
            return i
    raise NotFoundError(f'{excepted} not found in provided iterable')

class NotFoundError(Exception):
    pass
if __name__ == '__main__':
    print(find_in(['Rolf','Jen','Jose'], lambda x : x , 'Jose'))