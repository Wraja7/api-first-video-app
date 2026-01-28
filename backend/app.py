from flask import Flask
from config import Config
from flask_cors import CORS
from extensions.jwt import jwt

from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.video_routes import video_bp



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, supports_credentials=True)

    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(video_bp)

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app



if __name__ == "__main__":
    app = create_app()
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
        use_reloader=False
    )
