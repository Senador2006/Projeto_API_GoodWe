from flask import Blueprint, request, jsonify
from app.services.alexa_service import AlexaService

alexa_bp = Blueprint('alexa', __name__)
alexa_service = AlexaService()


@alexa_bp.route('/comando', methods=['POST'])
def processar_comando():
    data = request.get_json()

    if not data or 'comando' not in data:
        return jsonify({"status": "Error", "message": "Comando não fornecido."}), 400

    resposta = alexa_service.processar_comando(data['comando'])

    status_code = 200 if resposta["status"] == "OK" else 400
    return jsonify(resposta), status_code
