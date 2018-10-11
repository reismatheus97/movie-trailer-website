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

