from app.routes.activity_routes import activity_bp
from app.routes.candidate_routes import candidate_bp

def register_routes(app):
    """
    將所有的 Blueprint 註冊到 Flask App
    """
    app.register_blueprint(activity_bp)
    app.register_blueprint(candidate_bp)
