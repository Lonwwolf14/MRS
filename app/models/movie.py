from app.utils.database import get_db

class Movie:
    def __init__(self, id, title, genres, rating=None):
        self.id = id
        self.title = title
        self.genres = genres
        self.rating = rating

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id, title, genres FROM movies")
        return [Movie(*row) for row in cursor.fetchall()]

    @staticmethod
    def get_user_ratings(user_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT movie_id, rating FROM ratings WHERE user_id = ?", (user_id,))
        return dict(cursor.fetchall())
