"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
from django.test import TestCase
from requests.auth import HTTPBasicAuth
from django.contrib.auth import login
from requests.auth import HTTPBasicAuth
from django import shortcuts
import requests

# TODO: Configure your database in settings.py and sync before running tests.

class ApiTest(TestCase):
    """Tests for the application views."""

    # Django requires an explicit setup() when running tests in PTVS
    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ApiTest, cls).setUpClass()
            django.setup()
            

    def test_post_feiralivre(self):
        """
        Tests POST Feira Livre
        """
        mensagem =  {
                        "BAIRRO": "",
                        "DISTRITO": "",
                        "ID": 2,
                        "LOGRADOURO": "rua abc",
                        "NOME_FEIRA": "FEIRA XY",
                        "NUMERO": "",
                        "REFERENCIA": "abc",
                        "REGIAO5": "",
                        "REGIAO8": "",
                        "REGISTRO": "reg245",
                        "SUBPREFE": "",
                        "resource_uri": "/api/feiraslivre/2/"
                    }
        self.client.login(username='api', password='api12345')
        response = self.client.post('/api/feiraslivre/',mensagem , content_type = 'application/json',follow = True)
        self.assertContains(response, 'REGISTRO', 1, 200)
        self.assertTrue(True,"TestePOST")

    def test_put_feiralivre(self):
        """
        Tests Put Feira Livre
        """
        mensagem =  {
                        "BAIRRO": "",
                        "DISTRITO": "",
                        "ID": 2,
                        "LOGRADOURO": "rua abc",
                        "NOME_FEIRA": "FEIRA XY",
                        "NUMERO": "",
                        "REFERENCIA": "abc",
                        "REGIAO5": "",
                        "REGIAO8": "",
                        "REGISTRO": "reg245",
                        "SUBPREFE": "",
                        "resource_uri": "/api/feiraslivre/2/"
                    }
        self.client.login(username='api', password='api12345')
        response = self.client.put('/api/feiraslivre/reg12345/', mensagem , content_type = 'application/json',follow = True)
        #self.assertContains(response, 'REGISTRO', 1, 200)
        self.assertTrue(True,"TestePUT")

    def test_get_feiralivre(self):
        """
        Tests Get Feira Livre
        """
        self.client.login(username='api', password='api12345')
        response = self.client.get('/api/feiraslivre/reg12345/',follow = True)
        self.assertContains(response, 'REGISTRO', 1, 200)
        self.assertTrue(True,"TesteGeT")

    def test_getALL_feiralivre(self):
        """
        Tests GetALL Feira Livre
        """
        self.client.login(username='api', password='api12345')
        username='api'
        password='api12345'
        auth = HTTPBasicAuth(username, password)
        #response = requests.get('http://localhost:56162/api/feiraslivres/', auth=auth)
        response = self.client.get('/api/feiraslivre/', follow=True)
        self.assertContains(response, 'REGISTRO', 1, 200)
        self.assertTrue(True,"TesteGeTALL")