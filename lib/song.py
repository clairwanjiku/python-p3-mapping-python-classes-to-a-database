from config import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.id = None  # Initialize id as None for new instances
        self.name = name
        self.album = album

    def save(self):
        # Save the song to the database
        query = "INSERT INTO songs (name, album) VALUES (?, ?)"
        CURSOR.execute(query, (self.name, self.album))
        CONN.commit()
        # Retrieve the id of the newly inserted row and assign it to the object
        self.id = CURSOR.lastrowid

    @classmethod
    def create_table(cls):
        # Create the 'songs' table if it doesn't exist
        query = "CREATE TABLE IF NOT EXISTS songs (id INTEGER PRIMARY KEY, name TEXT, album TEXT)"
        CURSOR.execute(query)
        CONN.commit()

    @classmethod
    def create(cls, name, album):
        # Create a Song instance, save it, and return it
        song = cls(name, album)
        song.save()
        return song
