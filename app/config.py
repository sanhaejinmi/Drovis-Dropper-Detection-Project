import os
from dotenv import load_dotenv
load_dotenv()

SQLALCHEMY_DATABASE_URI = 'sqlite:///./drovis.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
FRONT_ORIGIN = os.environ.get("FRONT_ORIGIN")
