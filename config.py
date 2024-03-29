import os


class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JOB_API_URL =os.environ.get('JOB_API_URL')
    # Photos path
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    # Job api url
    JOB_API_URL = os.environ.get("JOB_API_URL")
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI_TEST")



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQL_URL")

    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
