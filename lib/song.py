song_genres = ["Rap", "Pop", "Rock"]

class Song:
    count=0
    genres=[]
    artists = [] 
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        type(self).add_song_to_count()
        type(self).add_to_genres(genre)
        type(self).add_to_artists(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
        if genre not in cls.genres:
            cls.genres.append(genre)
        
    @classmethod
    def add_to_artists(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
        if artist not in cls.genres:
            cls.artists.append(artist)
    
    
        
    


