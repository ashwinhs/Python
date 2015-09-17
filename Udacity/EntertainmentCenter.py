import media
import freshTomatoes
import urllib
import json
from getYoutubeURL import trailer_search

movieList = ["tt0114709", "tt0499549", "tt0111161", "tt0382932", "tt0068646", "tt0468569", "tt0110912", "tt0137523", "tt1392190"]
imdbAPIBaseURL="http://www.omdbapi.com/?i="
imdbAPIParams="&plot=short&r=json"

count = 0
movieDetails = []

for movieId in movieList:
    connection = urllib.urlopen(imdbAPIBaseURL+movieId+imdbAPIParams)
    response = connection.read()
    parsed_response = json.loads(response)
    trailerLink = trailer_search(parsed_response["Title"])
    movieDetails.append( media.Movie(parsed_response["Title"], parsed_response["Plot"], parsed_response["Poster"], trailerLink))
    

freshTomatoes.open_movies_page(movieDetails)