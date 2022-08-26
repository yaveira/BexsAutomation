from urllib.parse import urljoin
from utils.constants import URL_FAKEAPI, ENDPOINT_CONSULT, ENDPOINT_CREATE
import requests


class apiSettings:
    def __init__(self, context):
        apiSettings.__init__(self, context)

    def body_cadastro_produto(self):
        body_content = {
            "title": f"{self._root['active_outline'][0]}",
            "price": float(self._root['active_outline'][1]),
            "description": f"{self._root['active_outline'][2]}",
            "image": f"{self._root['active_outline'][3]}",
            "category": f"{self._root['active_outline'][4]}"
        }

        return body_content

    def cadastrar_produto(self):
        request_url = urljoin(URL_FAKEAPI, ENDPOINT_CREATE)

        headers_content = {
            'Content-type': 'application/json'
        }

        self.body_content = apiSettings.body_cadastro_produto(self)

        self.response = requests.post(url=request_url, data=headers_content, json=self.body_content)
        return self.response

    def consultar_produto(self):
        request_url = urljoin(URL_FAKEAPI, ENDPOINT_CONSULT)

        self.response = requests.get(url=request_url)
        return self.response
