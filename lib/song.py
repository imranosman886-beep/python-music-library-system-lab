class Song:
    count = 0
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1

        if genre not in Song.genre_count:
            Song.genre_count[genre] = 0

        Song.genre_count[genre] += 1

        if artist not in Song.artist_count:
            Song.artist_count[artist] = 0

        Song.artist_count[artist] += 1

    @classmethod
    def genres(cls):
        return cls.genre_count.keys()

    @classmethod
    def artists(cls):
        return cls.artist_count.keys()