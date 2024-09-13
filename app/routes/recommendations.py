# app/routes/recommendations.py

from flask import Blueprint, jsonify, request, render_template
from app.services.recommendation_service import get_recommendations

bp = Blueprint('recommendations', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/recommendations')
def get_movie_recommendations():
    genre = request.args.get('genre')
    n = request.args.get('n', default=10, type=int)
    start_year = request.args.get('start_year', type=int)
    end_year = request.args.get('end_year', type=int)
    min_rating = request.args.get('min_rating', default=0, type=float)
    
    recommendations = get_recommendations(genre, n, start_year, end_year, min_rating)
    return jsonify([{'id': r.id, 'title': r.title, 'rating': r.rating} for r in recommendations])
