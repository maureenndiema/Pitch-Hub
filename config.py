import os

class Config:
    debug = True
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maureen:1234@localhost/pitchhub'
    UPLOADED_PHOTOS_DEST='app/static/photos'

     #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   
class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maureen:1234@localhost/pitchhub'

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maureen:1234@localhost/pitchhub'
    
    
DEBUG = True
ENV = 'development'

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}