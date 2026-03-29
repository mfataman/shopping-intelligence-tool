import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('DATABASE_URI')
    API_KEY = os.environ.get('API_KEY')
    OTHER_SETTING = os.environ.get('OTHER_SETTING')

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or 'sqlite:///dev.db'

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or 'sqlite:///test.db'

class ProductionConfig(Config):
    DATABASE_URI = os.environ.get('PROD_DATABASE_URI') or 'mysql://user:password@localhost/prod'
