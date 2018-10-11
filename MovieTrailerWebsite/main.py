
import requests
import json
import string

import movie

import fresh_tomatoes

API_KEY = "394f3a8e67543449583d84bcef8634a0"


a = movie.Movie(0,
                "Toy Story",
                "A story about a guy and his toys that come to life",
                0,
                "https://images-na.ssl-images-amazon.com/images/I/91q0UP6%2BUTL._SY879_.jpg",
                "https://www.youtube.com/watch?v=KYz2wyBy3kc")

b = movie.Movie(1,
                "Avatar",
                "A marine on an alient planet",
                0,
                "https://m.media-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
                "https://www.youtube.com/watch?v=WNW9Wz7k4pM")

x = movie.Movie(2,
                "Toy Story",
                "A story about a guy and his toys that come to life",
                0,
                "https://images-na.ssl-images-amazon.com/images/I/91q0UP6%2BUTL._SY879_.jpg",
                "https://www.youtube.com/watch?v=KYz2wyBy3kc")

y = movie.Movie(3,
                "Avatar",
                "A marine on an alient planet",
                0,
                "https://m.media-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
                "https://www.youtube.com/watch?v=WNW9Wz7k4pM")

starWarsMovieArray = []
localMovieArray = [a, b, x, y]

response = requests.get("https://api.themoviedb.org/3/search/movie?api_key=" +
                        API_KEY +
                        "&query=Star%20Wars")

responseJson = json.loads(response.content)

i = 0
for item in responseJson['results']:
    # i += 1
    # if i == 12:
    #     break
    movie_id = item['id']
    movie_title = item['title'].encode("ascii", errors="ignore").decode()
    movie_storyline = item['overview']
    movie_popularity = item['popularity']
    poster_image_url = 'https://image.tmdb.org/t/p/w300' + item['poster_path']
    youtube_url = 'https://www.youtube.com/watch?v=KYz2wyBy3kc'

    movieInstance = movie.Movie(movie_id, movie_title, movie_storyline, movie_popularity, poster_image_url, youtube_url)
    starWarsMovieArray.append(movieInstance)

# movieId = responseJson['results'][10]['id']
# print(movieId)

starWarsMovieArray = sorted(starWarsMovieArray, key=lambda k: k['movie_popularity'], reverse=True)
fresh_tomatoes.open_movies_page(starWarsMovieArray)
