import imdb

def get_response(message: str) -> str:
    prefix = "%"
    p_message = message.lower()

    if p_message[0:1] !=prefix:
        return

    p_message = p_message[1:]
    if p_message == "say hi":
        return "Hey"

    if p_message == "say kosomko":
        return "kosomko"

    if p_message.__contains__('search'):
        m = p_message[7:]
        moviesDB = imdb.IMDb()
        movies = moviesDB.search_movie(m)

        ConesString = f'searching for {m}: \n'
        for movie in movies:
            ConesString = ConesString +f'{movie} \n'

        return ConesString

    if p_message.__contains__('top10'):


        moviesDB = imdb.IMDb()
        movies = moviesDB.get_top250_movies()

        ConesString =  f'Top 10 movies: \n'
        for i in range(10):
            ConesString = ConesString + f'{movies[i]} \n'

        return  ConesString


    if p_message.__contains__('category'):

        str = 'please choose a category: \n' \
              '1) Comody 😂\n'\
              '2) Romance 😍🧡\n' \
              '3) Drama 🎭\n' \
              '4) Animation 🪀\n' \
              '5) SCI-FI 🤖\n' \
              '6) Action 🔫\n' \
              '7) Mestery 🕵️\n' \
              '8) Adventure 🎢\n' \
              '9) Horror 👻\n' \
              '10) Crime 🚓\n' \
              '11) Fantazy 🦄\n' \
              '12) SuperHero 🦸\n' \
              '\nPlease write %Genres with the number refer to the category next to it' \


        return  str

    if p_message.__contains__('genres'):
        m = p_message[7:].strip()

        if m == '1':
            geners = "Comody"
        elif  m == "2":
            geners = "Romance"
        elif  m == "3":
            geners = "Drama"
        elif  m == "4":
            geners = "Animation"
        elif  m == "5":
            geners = "SCI-FI"
        elif  m == "6":
            geners = "Action"
        elif  m == "7":
            geners = "Mestery"
        elif  m == "8":
            geners = "Adventure"
        elif  m == "9":
            geners = "Horror"
        elif  m == "10":
            geners = "Crime"
        elif  m == "11":
            geners = "Fantazy"
        elif  m == "12":
            geners = "SuperHero"
        else:
            return f"Please insert a valide number {m} {geners}"

        moviesDB = imdb.IMDb()
        movies = moviesDB.get_top50_movies_by_genres(geners)
        TVshowes = moviesDB.get_top50_tv_by_genres(geners)

        ConesString =  f'Top 10 {geners} movies: \n'
        for i in range(10):
            ConesString = ConesString + f'{i+1}){movies[i]} \n'

        ConesString = ConesString + f'\nTop 10 {geners} TV showes:\n'
        for j in range(10):
            ConesString = ConesString + f'{j+1}){TVshowes[j]} \n'
        return  ConesString
