from flask import Blueprint, jsonify, request, render_template
import requests
from app.services.recommendation_service import get_recommendations, get_content_based_recommendations
from config.config import Config

bp = Blueprint('recommendations', __name__)

def fetch_movie_data(movie_id):
    url = f"{Config.TMDB_BASE_URL}/movie/{movie_id}?api_key={Config.TMDB_API_KEY}&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching movie data: {e}")
        return None

def search_movies(query):
    url = f"{Config.TMDB_BASE_URL}/search/movie?api_key={Config.TMDB_API_KEY}&language=en-US&query={query}&page=1&include_adult=false"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()['results']
    except requests.RequestException as e:
        print(f"Error searching movies: {e}")
        return []

def get_tmdb_recommendations(movie_id, n):
    url = f"{Config.TMDB_BASE_URL}/movie/{movie_id}/recommendations?api_key={Config.TMDB_API_KEY}&language=en-US&page=1"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()['results'][:n]
    except requests.RequestException as e:
        print(f"Error getting TMDB recommendations: {e}")
        return []

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/recommendations')
def get_movie_recommendations():
    genre = request.args.get('genre', '')
    n = request.args.get('n', default=10, type=int)
    start_year = request.args.get('start_year', type=int)
    end_year = request.args.get('end_year', type=int)
    min_rating = request.args.get('min_rating', default=0, type=float)
    title = request.args.get('title', '')

    if title:
        recommendations = get_recommendations_by_title(title, n, genre, min_rating)
    else:
        recommendations = get_recommendations_by_criteria(genre, n, start_year, end_year, min_rating)

    return jsonify(recommendations)

def get_recommendations_by_title(title, n, genre, min_rating):
    search_results = search_movies(title)
    if not search_results:
        return []

    movie_id = search_results[0]['id']
    tmdb_recommendations = get_tmdb_recommendations(movie_id, n)
    return [movie for movie in (process_movie(m, genre, min_rating) for m in tmdb_recommendations) if movie]

def get_recommendations_by_criteria(genre, n, start_year, end_year, min_rating):
    recommendations = get_recommendations(genre, n, start_year, end_year, min_rating)
    return [process_movie_from_db(r) for r in recommendations]

def process_movie(movie, genre, min_rating):
    movie_data = fetch_movie_data(movie['id'])
    if not movie_data:
        return None

    movie_genres = [g['name'] for g in movie_data['genres']]
    if (not genre or genre in movie_genres) and movie['vote_average'] >= min_rating:
        return {
            'id': movie['id'],
            'title': movie['title'],
            'poster_path': movie['poster_path'],
            'rating': movie['vote_average'],
            'genres': movie_genres,
            'overview': movie_data.get('overview', 'No overview available.')
        }
    return None

def process_movie_from_db(movie):
    movie_data = fetch_movie_data(movie.id)
    return {
        'id': movie.id,
        'title': movie.title,
        'rating': movie.rating,
        'genres': movie.genres,
        'poster_path': movie_data['poster_path'] if movie_data else None,
        'overview': movie_data.get('overview', 'No overview available.') if movie_data else 'No overview available.'
    }

@bp.route('/movie/<int:movie_id>')
def get_movie_details(movie_id):
    movie_data = fetch_movie_data(movie_id)
    if movie_data:
        return jsonify(movie_data)
    return jsonify({'error': 'Movie not found'}), 404

@bp.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not found'}), 404

@bp.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500
