##Add new movies to my collection
#List all the movies in my collection
#Find a movie by movie title

MENU_PROMPT = "\nEnter 'a' to add movie , 'l' to list your movies , 'f' to find a movie by the title , or 'q' to quit : "

movies = []


def add_movie():

    title = input("Please enter a title for this movie : ")
    director = input("Please enter a director for this movie : ")
    year = int(input("Please enter a year for this movie : "))

    movies.append({
    'title' : title ,
    'director' : director,
    'year' : year
    })

def show_movies():
    for movie in movies :
        print_movie(movie)

def print_movie(movie) :
    print(f"Title : {movie['title']}")
    print(f"Director : {movie['director']}")
    print(f" Release year : {movie['year']}")

def find_movie():
    search_title = input("Search movie title you're looking for :  ")
    for movie in movies :
        if movie['title'] == search_title :
            print_movie(movie)

user_options = {
    "a" : add_movie,
    "l" : show_movies,
    "f" : find_movie
}

def menu():
    selection = input(MENU_PROMPT)

    while selection!='q':
        if selection in user_options :
            selected_function = user_options[selection]
            selected_function()
        else :
            print("Unknown command. Please try again .")

        selection = input(MENU_PROMPT)


menu()