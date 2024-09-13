import unittest
from app.models.movie import Movie

class TestMovie(unittest.TestCase):
    def test_movie_creation(self):
        movie = Movie(1, "Test Movie", "Action,Drama")
        self.assertEqual(movie.id, 1)
        self.assertEqual(movie.title, "Test Movie")
        self.assertEqual(movie.genres, "Action,Drama")

if __name__ == '__main__':
    unittest.main()
