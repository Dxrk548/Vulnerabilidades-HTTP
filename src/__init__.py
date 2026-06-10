from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='../templates')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///laboratorio.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'token_secreto_para_sesiones_seguras_12345'

    db.init_app(app)

    from .main_routes import main_bp
    from .auth_routes import auth_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    @app.after_request
    def add_security_headers(response):
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        return response

    with app.app_context():
        db.create_all()

    return app