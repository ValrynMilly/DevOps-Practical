from unittest.mock import patch
from flask import url_for
import requests_mock
from flask_testing import TestCase
from application import routes
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_homepage(self):
        valuetoreturn = "irosAafkeilir"
        with patch('application.routes.requests.get') as mock_get:
            # getting successful response by 200 code
            mock_get.return_value.status_code = 200
            mock_get.return_value = valuetoreturn
            
            response = routes.namegenform_post()
            
        self.assertIn(response.text, valuetoreturn)