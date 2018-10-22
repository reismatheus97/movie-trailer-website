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

# Creating movie instances with the response results.
starWarsMoviesArray = []

# Fetch "TMDb" API with the API KEY with query = "Star Wars".
response = requests.get("https://api.themoviedb.org/3/search/movie?api_key=" + API_KEY + "&query=Star%20Wars")

# Parse the response to a JSON.
responseJson = json.loads(response.content)

# Extract the total number of pages from the response.
totalPages = responseJson['total_pages']

for currentPage in range(1, totalPages):
    # Only in the first page the request goes without "page" query string parameter.
    if currentPage != 1:
        response = requests.get("https://api.themoviedb.org/3/search/movie?api_key=" + API_KEY + "&query=Star%20Wars&page=" + str(currentPage))  # NOQA
        responseJson = json.loads(response.content)

    # For each item in results, create a Movie instance.
    for item in responseJson['results']:
        movie_id = item['id']
        movie_title = item['title'].encode("ascii", errors="ignore").decode()  # Removing non-ASCII chars.
        movie_storyline = item['overview']
        movie_popularity = item['popularity']
        vote_average = item['vote_average']
        poster_image_url = 'https://image.tmdb.org/t/p/w300' + str(item['poster_path'])
        movieInstance = movie.Movie(movie_id,
                                    movie_title,
                                    movie_storyline,
                                    movie_popularity,
                                    vote_average,
                                    poster_image_url,
                                    "")

        starWarsMoviesArray.append(movieInstance)

# Sort the movie array by the key "movie_popularity"
starWarsMoviesArray = sorted(starWarsMoviesArray, key=lambda k: k['movie_popularity'], reverse=True)

# Open the movie trailer website's page.
fresh_tomatoes.open_movies_page(starWarsMoviesArray)
