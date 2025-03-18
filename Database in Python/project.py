from utils import database

user_choice = """ 
Enter : 
- 'a' to add a new book 
- 'l' to list all books
- 'r' to mark book as read
- 'd' to delete a book
- 'q' to quit

Your choice :  """

def menu():
    database.create_book_table()
    user_input = input(user_choice)
    while user_input!= 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else :
            print("Unknown command . Please try again ! ")

        user_input = input(user_choice)


def prompt_add_book():
    name = input("Enter a name of book :")
    author = input("Enter a name of author :")
    database.add_book(name,author)

def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read']  else 'NO'
        print(f"{book['name']} by {book['author']}, read : {book['read']}")

def prompt_read_book():
    name = input("Enter a name of book :")
    database.mark_book_as_read(name)

def prompt_delete_book():
    name = input("Enter a name of book you wish to delete :")
    database.delete_book(name)

menu()