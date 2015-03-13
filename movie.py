import fresh_tomatoes
import media
import string

#Define the exectuable piece of code in a main function
def main():
    # Open the CSV file which contains the Movie list 
    movielist = open("movies.csv")
    movies = []
    # Loop through line by line for each movie,but making sure that the commented lines are ignored
    for movie in movielist:
        if not movie.startswith("#"):
            movieinfo = string.split(movie,",")
            movies.append(media.Movie(movieinfo[0], movieinfo[1],movieinfo[2], movieinfo[3],movieinfo[4],movieinfo[5] ))
    #Call the python module that manufactures the CSS and HTML and opens the web page, which displays the movies         
    fresh_tomatoes.open_movies_page(movies)

#Make sure that main in this script gets executed only when it is called with that intent and not otherwise.
if __name__ == '__main__':
    main()
