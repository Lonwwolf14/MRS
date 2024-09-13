import logging
from app.data_processing.demographic_filtering import get_top_movies
from app.data_processing.content_based_filtering import prepare_content_based_data, get_recommendations as get_content_recommendations
from app.models.movie import Movie

logging.basicConfig(level=logging.INFO)

df, cosine_sim, indices = prepare_content_based_data()

def get_recommendations(genre=None, n=10, min_rating=0):
    top_movies = get_top_movies(n * 2)
    logging.info(f"Retrieved {len(top_movies)} top movies")

    if top_movies.empty:
        logging.warning("No top movies retrieved")
        return []

    recommendations = [
        Movie(
            id=row['id'],
            title=row['title'],
            genres=row.get('genres', ''),
            rating=row.get('vote_average', 0)
        )
        for _, row in top_movies.iterrows()
    ]

    logging.info(f"Created {len(recommendations)} movie objects")

    if genre:
        recommendations = [movie for movie in recommendations if genre.lower() in movie.genres.lower()]
        logging.info(f"{len(recommendations)} movies after genre filter")

    if min_rating:
        recommendations = [movie for movie in recommendations if movie.rating >= min_rating]
        logging.info(f"{len(recommendations)} movies after rating filter")

    recommendations.sort(key=lambda x: x.rating, reverse=True)
    final_recommendations = recommendations[:n]
    logging.info(f"Returning {len(final_recommendations)} recommendations")

    if not final_recommendations:
        logging.warning("No recommendations found, returning top rated movies")
        return [Movie(id=row['id'], title=row['title'], genres=row.get('genres', ''), rating=row.get('vote_average', 0))
                for _, row in top_movies.head(n).iterrows()]

    return final_recommendations

def get_content_based_recommendations(title, n=10):
    content_recommendations = get_content_recommendations(title, df, cosine_sim, indices)
    logging.info(f"Retrieved {len(content_recommendations)} content-based recommendations")

    if content_recommendations.empty:
        logging.warning(f"No content-based recommendations found for '{title}'")
        return []

    recommendations = [
        Movie(
            id=df.loc[idx, 'id'],
            title=df.loc[idx, 'title'],
            genres=df.loc[idx, 'genres'],
            rating=df.loc[idx, 'vote_average']
        )
        for idx in content_recommendations.index[:n]
        if idx in df.index
    ]

    logging.info(f"Returning {len(recommendations)} content-based recommendations")
    return recommendations