# app/data_processing/demographic_filtering.py

import pandas as pd
import numpy as np

def load_and_process_data(file_path):
    # Load the data
    df = pd.read_csv(file_path)
    
    # Ensure required columns are present
    required_columns = ['id', 'title', 'vote_average', 'vote_count']
    if not all(column in df.columns for column in required_columns):
        raise ValueError("Missing required columns in the dataset")

    # Calculate C
    C = df['vote_average'].mean()
    
    # Calculate m
    m = df['vote_count'].quantile(0.9)
    
    # Filter movies based on m
    qualified_movies = df.copy().loc[df['vote_count'] >= m]
    
    def weighted_rating(x, m=m, C=C):
        v = x['vote_count']
        R = x['vote_average']
        return (v/(v+m) * R) + (m/(m+v) * C)
    
    # Calculate score
    qualified_movies['score'] = qualified_movies.apply(weighted_rating, axis=1)
    
    # Sort movies based on score
    qualified_movies = qualified_movies.sort_values('score', ascending=False)
    
    return qualified_movies[['id', 'title', 'vote_count', 'vote_average', 'score']]

def get_top_movies(n=10):
    file_path = 'data/movies_metadata.csv'  # Adjust this path as needed
    qualified_movies = load_and_process_data(file_path)
    return qualified_movies.head(n)
