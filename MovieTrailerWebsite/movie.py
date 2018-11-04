class Movie:
    """
    A class to represent a real movie.

    Parameters
    ----------
    movie_id          (str): an ID to be used to fetch TMDb and find a trailer;
    movie_title       (str): the movie title;
    movie_popularity  (str): the movie popularity;
    poster_image      (str): a URL to the movie poster;

    """
    def __init__(self, movie_id, movie_title, movie_popularity, poster_image):
        self.movie_id = movie_id
        self.movie_title = movie_title
        self.movie_popularity = movie_popularity
        self.poster_image_url = poster_image

    # Required to sort a list of movies.
    def __getitem__(self, item):
        return getattr(self, item)
