import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:121220@127.0.0.1:3306/holecover'
    SQLALCHEMY_TRACK_MODIFICATIONS = False