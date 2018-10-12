import requests
import json

import movie

import fresh_tomatoes

# API key to have access to "TMDb" API.
# This is NOT a comercial use about the API and all the credits
# belongs to TMDb, Inc. (https://www.themoviedb.org/).
# This key is registered to 'reismatheus97' and can't be used outside
# from this project and his purposes.
API_KEY = "394f3a8e67543449583d84bcef8634a0"

starWarsMoviesArray = []

# A movie array to be used when, for some reason,
# the results from "TMDb" API are not returned.
localMovieArray = movie.Movie.get_local_movie_array()

# Fetch "TMDb" API with the API KEY with query = "Star Wars".
response = requests.get("https://api.themoviedb.org/3/search/movie?api_key=" +
                        API_KEY +
                        "&query=Star%20Wars")

# Parse the response to a JSON.
responseJson = json.loads(response.content)

for item in responseJson['results']:
    movie_id = item['id']
    # Removing non-ASCII chars.
    movie_title = item['title'].encode("ascii", errors="ignore").decode()
    movie_storyline = item['overview']
    movie_popularity = item['popularity']
    poster_image_url = 'https://image.tmdb.org/t/p/w300' + item['poster_path']
    youtube_url = 'https://www.youtube.com/watch?v=KYz2wyBy3kc'

    movieInstance = movie.Movie(movie_id, movie_title, movie_storyline, movie_popularity, poster_image_url, youtube_url)
    starWarsMoviesArray.append(movieInstance)

starWarsMoviesArray = sorted(starWarsMoviesArray, key=lambda k: k['movie_popularity'], reverse=True)
fresh_tomatoes.open_movies_page(starWarsMoviesArray)
