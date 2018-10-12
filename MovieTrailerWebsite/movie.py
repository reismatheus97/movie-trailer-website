class Movie:
    def __init__(self, movie_id, movie_title, movie_storyline, movie_popularity, poster_image, trailer_youtube):
        self.movie_id = movie_id
        self.movie_title = movie_title
        self.movie_storyline = movie_storyline
        self.movie_popularity = movie_popularity
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def __getitem__(self, item):
        return getattr(self, item)


def get_local_movie_array():
    a = Movie(0,
                   "Toy Story",
                   "A story about a guy and his toys that come to life",
                   0,
                   "https://images-na.ssl-images-amazon.com/images/I/91q0UP6%2BUTL._SY879_.jpg",
                   "https://www.youtube.com/watch?v=KYz2wyBy3kc")

    b = Movie(1,
                   "Avatar",
                   "A marine on an alien planet",
                   0,
                   "https://m.media-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
                   "https://www.youtube.com/watch?v=WNW9Wz7k4pM")

    x = Movie(2,
                   "Toy Story",
                   "A story about a guy and his toys that come to life",
                   0,
                   "https://images-na.ssl-images-amazon.com/images/I/91q0UP6%2BUTL._SY879_.jpg",
                   "https://www.youtube.com/watch?v=KYz2wyBy3kc")

    y = Movie(3,
                   "Avatar",
                   "A marine on an alient planet",
                   0,
                   "https://m.media-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
                   "https://www.youtube.com/watch?v=WNW9Wz7k4pM")

    return [a, b, x, y]

