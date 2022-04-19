class Song():
    def __init__(self, length, title, author, views, path):
            self.length = length
            self.title = title
            self.author = author
            self.views = views
            self.path = path

    def song_stats(self, length, title, author, views, path):
    # time, grab song data from spotify api or tunebat
        print("Name: "+title+" - "+author)
        print("Length: "+seconds_to_minutes(length))
        print("Listens: "+str(views))
        print('Download Path: '+ path)
        print('success')
    # https://developer.spotify.com/documentation/web-api/reference/#/operations/get-several-audio-features
    # https://medium.com/swlh/spotify-song-prediction-and-recommendation-system-b3bbc71398ad

