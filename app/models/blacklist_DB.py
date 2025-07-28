from app.db import db

class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 로그아웃, 블랙리스트 토큰 고유 식별자   
    jti = db.Column(db.String(36), nullable=False, index=True)
    # 토큰 차단된 시간
    created_at = db.Column(db.DateTime, nullable=False)