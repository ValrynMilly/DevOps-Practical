from unittest.mock import patch
from flask import url_for
import requests_mock
from flask_testing import TestCase
from application import routes
from application import app
from application.routes import namegenform_post

class TestBase(TestCase):
    def create_app(self):
        return app

class TestGenerate(TestBase):
    def test_ifpagefound(self):
        with patch('requests.get') as mock_request:
            servicetwo = 'http://service-two:5001'
            mock_request.return_value.result = "Fake content"
            response = namegenform_post()
            self.assertNotNone(response.result)