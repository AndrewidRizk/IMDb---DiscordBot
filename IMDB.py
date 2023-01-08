import imdb

moviesDB = imdb.IMDb()

def Search_movie(m):
    movies = moviesDB.search_movie(m)
    print("searching for inception: ")
    for movie in movies:
        print(f'{movie}')


