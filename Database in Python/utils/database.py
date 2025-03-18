'''
Concerned with storing and retrieving books from a list

name,author,read - FORMAT OF BOOKS IN FILE

file.readlines() - give us format with backslash
'''

## import json

from .database_connection import DatabaseConnection

#books_file = 'books.json'

def create_book_table():
    with DatabaseConnection('data.db') as connection :
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key , author text, read integer)')

def add_book(name,author) :
    '''
    books = get_all_books()
    books.append({'name' : name , 'author' : author , 'read' : False})
    _save_all_books(books) WAY WITH JSON FORMAT
    '''
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'INSERT INTO books VALUES(?,?,0)',(name,author))

def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'SELECT * FROM books')
        books = [{"name" : row[0] , "author" : row[1] , "read" : row[2]} for row in cursor.fetchall()]

    return  books

''' 
def _save_all_books(books):
    with open(books_file, 'w') as file :
        json.dump(books,file)
'''


def mark_book_as_read(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'UPDATE books SET read = 1 WHERE name = ? ' , (name,))

    '''
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_all_books(books)
    '''

def delete_book(name):
    '''

    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)
    '''

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute(f'DELETE * FROM books WHERE name = ? ' , (name,))