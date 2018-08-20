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
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_strong_key')
    BCRYPT_HASH_PREFIX = 14
    SQLALCHEMY_TRACK_MODIFICATION = False
    AUTH_TOKEN_EXPIRY_DAYS = 30
    AUTH_TOKEN_EXPIRY_SECOND = 3000
    BUCKET_AND_ITEMS_PER_PAEG = 25

class DevelopmentConfig(BaseConfig):
    """
    Development application configuration
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', postgres_local_base+database_name)
    BCRYPT_HASH_PREFIX = 4
    AUTH_TOKEN_EXPIRY_DAYS=1
    AUTH_TOKEN_EXPIRY_SECOND = 20
    BUCKET_AND_ITEMS_PER_PAEG = 4

class TestingConfig(BaseConfig):
    """
    Testing application configuration
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_TEST', postgres_local_base+database_name)
    BCRYPT_HASH_PREFIX = 4
    AUTH_TOKEN_EXPIRY_DAYS = 0
    AUTH_TOKEN_EXPIRY_SECOND=3
    AUTH_TOKEN_EXPIRATION_TIME_DURING_TESTS = 5
    BUCKET_AND_ITEMS_PER_PAEG = 3

class ProductionConfig(BaseConfig):
    """
    Production application configuration
    """

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', postgres_local_base+database_name)
    BCRYPT_HASH_PREFIX=13
    AUTH_TOKEN_EXPIRY_DAYS=30
    AUTH_TOKEN_EXPIRY_SECOND=20
    BUCKET_AND_ITEMS_PER_PAEG = 10