from unittest.mock import patch
from flask import url_for
import requests_mock
from flask_testing import TestCase
from application import routes
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestGenerate(TestBase):
    def test_homepage(self):
        with requests_mock.mock() as mock_get:
            # getting successful response by 200 code
            mock_get.get("http://service-two:5001", text="irosAafkeilir")
            response = self.client.post(url_for('namegenform_post'))
            
            self.assertIn(b'irosAafkeilir', response)