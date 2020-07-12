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
            mock_request.return_value.text = "ilir"
            response = namegenform_post()
            self.assertNotNone(response.result.text)