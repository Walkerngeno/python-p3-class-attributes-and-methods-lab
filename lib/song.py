class Song:
    # Class variable to count the number of Song objects
    count = 0

    # Class variable to keep track of all Song genres
    genres = set()

    # Class variable to keep track of all Song artists
    artists = set()

    # Class variable to keep count of Songs for each genre
    genre_count = {}

    # Class variable to keep count of Songs for each artist
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the count when a new Song object is created
        Song.count += 1

        # Add the genre to the set of genres
        Song.genres.add(self.genre)

        # Add the artist to the set of artists
        Song.artists.add(self.artist)

        # Update genre count
        Song.genre_count[self.genre] = Song.genre_count.get(self.genre, 0) + 1

        # Update artist count
        Song.artist_count[self.artist] = Song.artist_count.get(self.artist, 0) + 1
