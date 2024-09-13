import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATABASE_PATH = os.path.join(BASE_DIR, '..', 'data', 'movies.db')
    MOVIES_METADATA_PATH = os.path.join(BASE_DIR, '..', 'data', 'tmdb_5000_movies.csv')
    CREDITS_PATH = os.path.join(BASE_DIR, '..', 'data', 'tmdb_5000_credits.csv')
