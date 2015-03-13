class Movie(object):
    """Movie class serves as a data structure that stores the following attributes of a movie trailer
    Attributes:
        title ::  Movie Title
        storyline :: Story Line of Movie
        hero :: Hero of the Movie
        release_year :: Release year of the movie
        poster_image_url :: URL to the poster image of movie
        youtube_url ::  URL to the youtube movie trailer 
    """
    def __init__(self,movie_title, movie_storyline, movie_hero, movie_releaseyear,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.hero = movie_hero
        self.release_year = movie_releaseyear
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube