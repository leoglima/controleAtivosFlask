from dotenv import load_dotenv
import os

load_dotenv() 


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FIREBASE_URL = os.environ.get('FIREBASE_URL')
