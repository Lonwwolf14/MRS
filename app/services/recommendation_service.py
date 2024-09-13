# app/services/recommendation_service.py

from app.data_processing.demographic_filtering import get_top_movies
from app.models.movie import Movie

def get_recommendations(genre=None, n=10, start_year=None, end_year=None, min_rating=0):
    # Use demographic filtering for all recommendations
    top_movies = get_top_movies(n)
    
    # Convert DataFrame rows to Movie objects
    recommendations = [
        Movie(
            id=row['id'], 
            title=row['title'], 
            genres=row.get('genres', ''),  # Use empty string if genres not available
            rating=row['vote_average']
        ) 
        for _, row in top_movies.iterrows()
    ]
    
    # Apply additional filters if specified
    if genre:
        recommendations = [movie for movie in recommendations if genre.lower() in movie.genres.lower()]
    if start_year:
        recommendations = [movie for movie in recommendations if movie.year and movie.year >= start_year]
    if end_year:
        recommendations = [movie for movie in recommendations if movie.year and movie.year <= end_year]
    if min_rating:
        recommendations = [movie for movie in recommendations if movie.rating >= min_rating]
    
    return recommendations[:n]  # Ensure we return at most n recommendations

# Content-based filtering code (commented out)
"""
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
"""
