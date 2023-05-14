import os

from dotenv import load_dotenv

from blog.enums import EnvType

load_dotenv()

ENV = os.getenv('FLASK_ENV', default=EnvType.PRODUCTION)
DEBUG = ENV == EnvType.DEVELOPMENT

SECRET_KEY = os.getenv('SECRET_KEY')

API_URL = os.getenv('API_URL')

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True

OPENAPI_URL_PREFIX = '/api/docs'
OPENAPI_VERSION = '3.0.0'
OPENAPI_SWAGGER_UI_PATH = '/'
OPENAPI_SWAGGER_UI_VERSION = '3.51.1'
