from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestGen(TestBase):
    def test_generate(self):
        with patch('requests.get') as g:
            g.return_value = "Adairisaren"
            with patch('requests.post') as p:
                p.return_value.text = "A Omnipotent Born"
                response = self.client.get('/')
                self.assertIn(b'Adairisaren A Omnipotent Born', response.data)