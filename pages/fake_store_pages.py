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
            "title": f"{self._root['active_outline'][0]}",
            "price": float(self._root['active_outline'][1]),
            "description": f"{self._root['active_outline'][2]}",
            "image": f"{self._root['active_outline'][3]}",
            "category": f"{self._root['active_outline'][4]}"
        }

        self.response = requests.post(url=request_url, data=headers_content, json=body_content)
        return self.response, body_content

    def consultar_produto(self):
        request_url = urljoin(URL_FAKEAPI, API_CONSULT)

        self.response = requests.get(url=request_url)
        return self.response, self.response