"""configuration for app"""
import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    """class configuration"""
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATION = False
