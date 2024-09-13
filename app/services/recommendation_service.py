from app.models.movie import Movie
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def content_based_recommendations(user_id, n=5):
    movies = Movie.get_all()
    user_ratings = Movie.get_user_ratings(user_id)

    # Create a matrix of movie genres
    genres = [movie.genres for movie in movies]
    vectorizer = CountVectorizer()
    genre_matrix = vectorizer.fit_transform(genres)

    # Calculate cosine similarity between movies
    cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

    # Get the indices of movies the user has rated
    rated_movie_indices = [movie.id - 1 for movie in movies if movie.id in user_ratings]

    # Calculate the average similarity score for each movie
    sim_scores = cosine_sim[rated_movie_indices].mean(axis=0)

    # Get the indices of the top N similar movies
    top_indices = sim_scores.argsort()[::-1][:n]

    # Return the recommended movies
    recommendations = [movies[i] for i in top_indices if movies[i].id not in user_ratings]
    return recommendations
