from flask import Blueprint, jsonify
from app.services.goodwe_service import GoodWeService

goodwe_bp = Blueprint('goodwe', __name__)
goodwe_service = GoodWeService()

@goodwe_bp.route('/status', methods=['GET'])
def status():
    status = goodwe_service.obter_status_inversor()
    return jsonify(status)

@goodwe_bp.route('/producao', methods=['GET'])
def producao():
    producao = goodwe_service.obter_producao_energia()
    return jsonify(producao)
