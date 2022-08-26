from sys import stdout
from urllib.parse import urljoin
from utils.constants import URL_FAKEAPI, API_CONSULT, API_CREATE
import requests
import json


class FakeApi:
    def __init__(self, context):
        FakeApi.__init__(self, context)

    def criar_produto(self):
        request_url = urljoin(URL_FAKEAPI, API_CREATE)

        headers_content = {
            'Content-type': 'application/json'
        }

        body_content = {
            "title": "iphone 12 64GB",
            "price": 5000.5,
            "description": "Iphone 12 64GB cor preto",
            "image": "https: //i.pravatar.cc",
            "category": "celulares"
        }

        self.response = requests.post(url=request_url, headers_content=headers_content, body=body_content)
        a = json.loads(self.response.text)
        return self.response

    def consultar_produto(self):
        request_url = urljoin(URL_FAKEAPI, API_CONSULT)

        self.response = requests.get(url=request_url)
        a = json.loads(self.response.text)
        return self.response