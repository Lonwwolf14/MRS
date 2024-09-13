import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from ast import literal_eval
from config.config import Config
import logging

logging.basicConfig(level=logging.INFO)

def prepare_content_based_data():
    df1 = pd.read_csv(Config.CREDITS_PATH, low_memory=False)
    df2 = pd.read_csv(Config.MOVIES_METADATA_PATH, low_memory=False)

    df1['id'] = df1['id'].astype(str)
    df2['id'] = df2['id'].astype(str)

    df = pd.merge(df2, df1, on='id')
    logging.info(f"Merged dataframe shape: {df.shape}")

    if 'title' not in df.columns:
        if 'original_title' in df.columns:
            df['title'] = df['original_title']
        else:
            df['title'] = 'Unknown Title'

    df['overview'] = df['overview'].fillna('')
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['overview'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    features = ['cast', 'crew', 'keywords', 'genres']
    for feature in features:
        df[feature] = df[feature].apply(safe_literal_eval)

    df['director'] = df['crew'].apply(get_director)
    for feature in ['cast', 'keywords', 'genres']:
        df[feature] = df[feature].apply(get_list)

    features = ['cast', 'keywords', 'director', 'genres']
    for feature in features:
        df[feature] = df[feature].apply(clean_data)

    df['soup'] = df.apply(create_soup, axis=1)

    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(df['soup'])
    cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

    df = df.reset_index()
    indices = pd.Series(df.index, index=df['title'])

    logging.info("Content-based data preparation completed")
    return df, cosine_sim2, indices

def get_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
    return np.nan

def get_list(x):
    if isinstance(x, list):
        names = [i['name'] for i in x]
        return names[:3] if len(names) > 3 else names
    return []

def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    elif isinstance(x, str):
        return str.lower(x.replace(" ", ""))
    else:
        return ''

def create_soup(x):
    return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres'])

def get_recommendations(title, df, cosine_sim, indices):
    idx = indices.get(title)
    if idx is None:
        logging.warning(f"Title '{title}' not found in the dataset")
        return pd.Series()
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

def safe_literal_eval(val):
    try:
        return literal_eval(val)
    except (ValueError, SyntaxError):
        return []
