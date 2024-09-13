from flask import Blueprint, jsonify, request, render_template
from app.services.recommendation_service import content_based_recommendations

bp = Blueprint('recommendations', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/recommendations/<int:user_id>')
def get_recommendations(user_id):
    n = request.args.get('n', default=5, type=int)
    recommendations = content_based_recommendations(user_id, n)
    return jsonify([{'id': r.id, 'title': r.title, 'genres': r.genres} for r in recommendations])
