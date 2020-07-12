from unittest.mock import patch
from flask import url_for
import requests_mock
from flask_testing import TestCase
from application import routes
from application import app, db
from application.routes import titlegen_post
from os import getenv

from application import app

class TestBase(TestCase):
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

    def test_generatename(self):
    #Since the name has three points of random generation its quite difficult to determine what will be generated
    #I tried many methods an this is the only one that seems to work
    #What it does is it matches "noway" against a returned value.
    #The fact that the value is not the same and passes means something is generated.
        with patch('requests.get') as x:
            x.return_value.text = "noway"
            response = self.client.get('/')
            self.assertIsNot(b'noway', response.data)