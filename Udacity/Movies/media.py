import webbrowser, urllib
class Video():
    def __init__(self, title):
        self.title = title
        
class Movie(Video):
    """Idu Namma Movie Classu. Moviegala list holdings madokke bardirodhu!!!"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
        
    def __init__(self, title, storyline, poster, trailerlink):
        Video.__init__(self, title)
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailerlink
    
    def showTrailer(self):
        webbrowser.open_new(self.trailer_youtube_url)

    def showPoster(self):
        webbrowser.open_new(self.poster_image_url)
        
        