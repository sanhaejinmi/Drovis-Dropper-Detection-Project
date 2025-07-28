from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.db import db
from app.routes.auth import auth_bp
from app.config import *
from app.models.blacklist_DB import TokenBlocklist
from datetime import datetime

jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI,
        SQLALCHEMY_TRACK_MODIFICATIONS=SQLALCHEMY_TRACK_MODIFICATIONS,
        JWT_SECRET_KEY=JWT_SECRET_KEY,
    )

    db.init_app(app)
    jwt.init_app(app)

    CORS(app, resources={r"/*": {"origins": FRONT_ORIGIN}}, supports_credentials=True)
    app.register_blueprint(auth_bp)

    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        return TokenBlocklist.query.filter_by(jti=jti).first() is not None

    return app
