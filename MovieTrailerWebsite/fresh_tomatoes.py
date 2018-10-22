import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Star Wars Movie Trailer Website</title>
    
    <script type="text/javascript" charset="utf-8"> 
        // API key to have access to "TMDb" API.
        // This is NOT a comercial use about the API and all the credits
        // belongs to TMDb, Inc. (https://www.themoviedb.org/).
        // This key is registered to 'reismatheus97' and can't be used outside
        // from this project and his purposes.

        const API_KEY = "394f3a8e67543449583d84bcef8634a0"
    </script>
    
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.18.0/axios.min.js"></script>
    
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 25px;
            margin-top: 10px;
            padding-top: 10px;
            min-height: 520px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .error-msg {
            text-align: center;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
    
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var movieTmdbId = $(this).attr('data-tmdb-movie-id')
            
            // Fetch TMDb api to get the youtube trailer id.
            axios.get(`https://api.themoviedb.org/3/movie/${movieTmdbId}/videos?api_key=${API_KEY}`, { method: 'GET' })
            .then( response => {
                let results = response
                    .data
                    .results
                    .sort(function (a, b) { // Sort results increasingly
                        if (a.type > b.type) {
                            return -1;
                        }
                        if (a.type < b.name) {
                            return 1;
                        }
                        return 0;
                    });
                
                return results[0].key
            })
            .catch( err => {
                $("#trailer-video-container").empty().append($("<h3 class='error-msg'>No trailer available for this video. :( </h3>"))
                debugger;
                console.warn("Failed on fetch", err)
                return 0;
            }).then( trailerYouTubeId => {
                if (trailerYouTubeId != 0) {
                    var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
                    $("#trailer-video-container").empty().append($("<iframe></iframe>", {
                        'id': 'trailer-video',
                        'type': 'text-html',
                        'src': sourceUrl,
                        'frameborder': 0
                    }));
                }                    
            }).catch(
                err => {
                    console.warn("Failed on fetch youtube trailer", err)
                    $("#trailer-video-container").empty().append($("<h3 class='error-msg'>No trailer available for this video. :( </h3>"))
                }
            )
        });
        
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header" style="width: 100%;">
            <a class="navbar-brand" href="#">The Star Wars Collection Trailers</a>
            <div style="float: right;">
                <a class="navbar-brand" 
                   href="https://www.themoviedb.org/"
                   style="float: right; text-decoration: underline;">
                     Powered by TheMovieDB API.
                </a>
            </div>
          </div>
          
        </div>
      </div>
    </div>
    <div class="container movies-container">
        {movie_tiles}
    </div>
    <hr/>
    <div style="text-align: center;">
        <h2><a href="https://www.starwars.com/">The official Star Wars site.</a></h2>
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-tmdb-movie-id="{movie_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    # trailer_youtube_id = ''

    for index, movie in enumerate(movies):

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_id=movie.movie_id,
            movie_title=movie.movie_title,
            poster_image_url=movie.poster_image_url
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)