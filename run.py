from flask import Flask
from app.routes.alexa_routes import alexa_bp
from app.routes.goodwe_routes import goodwe_bp
from app.routes.suggestion_routes import suggestion_bp

def create_app():
    app = Flask(__name__)

    # Registrando os Blueprints
    app.register_blueprint(alexa_bp, url_prefix='/alexa')
    app.register_blueprint(goodwe_bp, url_prefix='/goodwe')
    app.register_blueprint(suggestion_bp, url_prefix='/sugestoes')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
