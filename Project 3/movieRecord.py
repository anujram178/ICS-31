#Ramaswamy, Anuj
from collections import namedtuple
movieList = []
def addMovies(y,t,r,d):
    '''This command takes 4 arguments: the year released , the movie title, Rottentomatoes rating (a float), and the directors name, separated by
    commas. This command adds the information about the new movie into the system. 
    '''
    movierecord = namedtuple("movierecord", "year title rating director")
    movierecord.year = int(y)
    movierecord.title = t
    movierecord.rating = float(r)
    movierecord.director = d
    movieList.append(movierecord)
    
def deleteMovie(movie):
    '''This command deletes the information of the given movie from the system.'''
    for movieInfo in movieList:
        if movieInfo.title == movie:
            movieList.remove(movieInfo)

def printOneMovie(movie):
    '''This function prints all the information of the movie given as the argument and is used as a helper function for the commands.'''
    print(f"{movie.title}, {movie.year}, {movie.rating}, {movie.director}")
    
def printMovie():
    '''This command prints all the movie in the system.'''
    for movie in movieList:
        printOneMovie(movie)

def findRotten(IMDB):
    '''This command prints all movies below the rating given.'''
    for movierecord in movieList:
        if movierecord.rating < float(IMDB):
            printOneMovie(movierecord)

def findMovie(movie):
    '''This command prints the information about the particular movie given as the argument.'''
    for movierecord in movieList:
        if movie in movierecord.title:
            print(f"{movierecord.year}, {movierecord.rating}, {movierecord.director}")

def selectRating(movierecord):
    '''This function helps to sort the movies in the system based on rating of the movies.'''
    return movierecord.rating

def sortRating():
    '''This command sorts the movies in the system based on the rating and prints all the information of all movies in the system.'''
    movieList.sort(key = selectRating, reverse= True)
    printMovie()

def mdbase():
    '''This is the main function which calls all other functions and takes input from the user and performs the tasks based on what the user types.'''
    print("addmovie, deletemovie, sortratings, findrotten, findmovie, printmovies, quit")
    program = 1
    while program == 1:
        userInput = input("$ ")
        commandList = userInput.split()
        if commandList[0]== 'addmovie':
            dataList = userInput.split(',')
            dataList[0] = dataList[0].split()[1]
            for i in range(len(dataList)):
                dataList[i] = dataList[i].strip()
            yearInput = dataList[0]
            titleInput = dataList[1]
            ratingInput = dataList[2]
            dirInput = dataList[3]
            addMovies(yearInput, titleInput,ratingInput,dirInput)
        elif commandList[0] == "deletemovie":
            MovieToDelete = userInput[12:]
            deleteMovie(MovieToDelete)
        elif commandList[0] == "printmovies":
            printMovie()
        elif commandList[0] == "findrotten":
            RatingThreshold = userInput[11:]
            findRotten(RatingThreshold)
        elif commandList[0] == "findmovie":
            MovieToFind = userInput[10:]
            findMovie(MovieToFind)
        elif commandList[0] == "sortratings":
            sortRating()
        elif commandList[0] == "quit":
            program = 0
            print("you ended the program")               
mdbase()
