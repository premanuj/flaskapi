import os
base_dir = os.path.abspath(os.path.dirname(__name__))
# postgres_local_base = 'mssql+pymssql://SA:Pr3m@nuj@localhost/'
postgres_local_base = 'postgresql://postgres:postgres@localhost/'
database_name = 'flaskapi'


class BaseConfig:
    """
    
    Base application configuration

    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_strong_key')
    SQLALCHEMY_TRACK_MODIFICATION = False

class DevelopmentConfig(BaseConfig):
    """
    Development application configuration
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', postgres_local_base+database_name)
    

class TestingConfig(BaseConfig):
    """
    Testing application configuration
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_TEST', postgres_local_base+database_name)


class ProductionConfig(BaseConfig):
    """
    Production application configuration
    """

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', postgres_local_base+database_name)