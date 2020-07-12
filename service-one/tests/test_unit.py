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

    def test_generate(self):
        with patch('requests.get') as g:
            g.return_value.text = "irosaafkeilir"
            with patch('requests.get') as p:
                p.return_value.text = " THE OMNIBENEVOLENT BERZERKER"
                with patch('requests.get') as d:
                    d.return_value.text = "ONCE ANNIHILATED 1089 MEN WITH FIRE"
                response = self.client.get('/')
                self.assertIn(b'IN A BAR irosaafkeilir THE OMNIBENEVOLENT BERZERKER ONCE ANNIHILATED 1089 MEN WITH FIRE', response.data)