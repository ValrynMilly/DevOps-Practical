from unittest.mock import patch
from flask import url_for
import requests_mock
from flask_testing import TestCase
from application import routes
from application import app, db
from application.routes import namegenform_post
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        return app
    
    def create_app(self):
    
        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app


class TestGenerate(TestBase):

    def test_homeview(self):
        response = self.client.get('/')
        self.assertIn(b"submit", response.data)

    def test_generatename(self):
        with patch('requests.get') as p:
            p.return_value.text = "ilir"
            response = self.client.post('/')
            self.assertIn(b'ilir', response.data)

    def test_generatetitle(self):
        with patch('requests.get') as x:
            x.return_value.text = "A OMNIPOTENT BORN"
            response = self.client.post('/')
            self.assertIn(b'A OMNIPOTENT BORN', response.data)
            
