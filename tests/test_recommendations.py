import unittest
from app.services.recommendation_service import content_based_recommendations

class TestRecommendations(unittest.TestCase):
    def test_content_based_recommendations(self):
        recommendations = content_based_recommendations(1, n=3)
        self.assertEqual(len(recommendations), 3)
        self.assertTrue(all(isinstance(r, Movie) for r in recommendations))

if __name__ == '__main__':
    unittest.main()
