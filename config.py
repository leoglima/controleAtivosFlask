import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    FIREBASE_URL = "https://controle-de-ativos-spv-default-rtdb.firebaseio.com/Ativos_Cadastrados/.json"
