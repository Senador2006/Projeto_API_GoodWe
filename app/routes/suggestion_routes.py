from flask import Blueprint, jsonify
from app.services.suggestion_service import SuggestionService

suggestion_bp = Blueprint('suggestion', __name__)
suggestion_service = SuggestionService()

@suggestion_bp.route('/clima', methods=['GET'])
def clima():
    sugestao = suggestion_service.obter_sugestao_clima()
    return jsonify({'sugestao': sugestao})
