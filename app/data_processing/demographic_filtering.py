import pandas as pd
import numpy as np
from config.config import Config

def load_and_process_data():
    df1 = pd.read_csv(Config.CREDITS_PATH, low_memory=False)
    df2 = pd.read_csv(Config.MOVIES_METADATA_PATH, low_memory=False)

    df1['id'] = df1['id'].astype(str)
    df2['id'] = df2['id'].astype(str)

    df = pd.merge(df2, df1, on='id', how='inner')
    
    # Select columns flexibly
    id_col = 'id'
    title_col = 'original_title' if 'original_title' in df.columns else 'title'
    vote_count_col = 'vote_count'
    vote_average_col = 'vote_average'
    
    df = df[[id_col, title_col, vote_count_col, vote_average_col, 'cast', 'crew']]
    df = df.rename(columns={title_col: 'title'})

    # Rest of the function remains the same
    C = df['vote_average'].mean()
    m = df['vote_count'].quantile(0.9)

    q_movies = df.copy().loc[df['vote_count'] >= m]

    def weighted_rating(x, m=m, C=C):
        v = x['vote_count']
        R = x['vote_average']
        return (v/(v+m) * R) + (m/(m+v) * C)

    q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
    q_movies = q_movies.sort_values('score', ascending=False)

    return q_movies[['id', 'title', 'vote_count', 'vote_average', 'score']]




def get_top_movies(n=10):
    qualified_movies = load_and_process_data()
    return qualified_movies.head(n)
