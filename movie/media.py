import webbrowser

class Movie():
    def __init__(self, mTitle, posterImage, trailerYoutube):
        self.title = mTitle
        self.posterUrl = posterImage
        self.trailerUrl = trailerYoutube

    def show_trailer(self):
        webbrowser.open(self.trailerUrl)
