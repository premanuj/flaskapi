"""

This file test a various configuration of the flask app

This test is preety standard no need to make change unless the app configuration change take place

App testing module

Module used:
    os
    unittest
    app
    flask_testing > TestCase

"""

import os
import unittest
from flask_testing import TestCase
from app import app

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.DevelopmentConfig')
        return app 
    
    def test_app_development(self):
        self.assertTrue(app.config['SERECT_KEY']==os.getenv('SECRET_KEY'))
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(app is None)
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'==os.environ.get('DATABASE_URL')])


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.TestingConfig')
        return app 
    
    def test_app_testing(self):
        self.assertTrue(app.config['SERECT_KEY']==os.getenv('SECRET_KEY'))
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])
        # self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXPECTION'])
        self.assertTrue(app.config['SQLALCHEMY_DATABASE_URI'==os.environ.get('DATABASE_URL_TEST')])

class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.ProductionConfig')
        return app

    def test_app_production(self):
        self.assertTrue(app.config['SECRET_KEY']==os.getenv('SECRET_KEY'))
        self.assertFalse(app.config['DUBUG'])
        self.assertFalse(app.config['TESTING'])


if __name__ == "__main__":
    unittest.main()
