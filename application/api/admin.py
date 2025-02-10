from flask import jsonify
from flask import request
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

def require_api_key(func):
    def wrapper(*args, **kwargs):
        api_key_aut = request.headers.get('X-API-KEY')
        if not api_key_aut or api_key_aut != str(SECRET_KEY):
            return jsonify({'error': 'Access denied'}), 401
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper
