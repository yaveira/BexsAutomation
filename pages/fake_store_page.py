from utils.api_settings import apiSettings
from hamcrest import assert_that, equal_to
from json import loads

class fakeStorePage:
    def __init__(self, context):
        fakeStorePage.__init__(self, context)

    def consultar_produtos(self):
        self.lista_produtos = apiSettings.consultar_produto(self)

    def validar_status_code(self, status_code):
        assert_that(int(status_code), equal_to(self.lista_produtos.status_code))

    def validar_quantidade_produtos(self, quantidade_produto):
        convertendo_lista_produtos = loads(self.lista_produtos.text)
        tamanho_lista_produtos = len(convertendo_lista_produtos)
        assert_that(int(quantidade_produto), equal_to(tamanho_lista_produtos))

    def validar_dados_produtos(self, nome_produto, valor_produto):
        lista_produtos = loads(self.lista_produtos.text)
        tamanho_lista_produtos = len(lista_produtos)

        if tamanho_lista_produtos >= 1:
            for i in range(tamanho_lista_produtos):
                if lista_produtos[i]['title'] == nome_produto and lista_produtos[i]['price'] == float(valor_produto):
                    assert_that(nome_produto, equal_to(lista_produtos[i]['title']))
                    assert_that(float(valor_produto), equal_to(lista_produtos[i]['price']))
        else:
            raise AssertionError('Name and value is not present')

    def cadastro_produtos(self):
        self.lista_produtos = apiSettings.cadastrar_produto(self)

    def validar_produtos_cadastrados(self, tipo_dado_produto):
        assert_that(self.table[0][f'{tipo_dado_produto}'], equal_to(str(self.body_content[f'{tipo_dado_produto}'])))

    def validar_id_produto(self):
        id_produto_cadastrado = loads(self.lista_produtos.text)['id']
        consultar_id_ultimo_produto_cadastrado = len(loads(apiSettings.consultar_produto(self).text)) + 1

        assert_that(consultar_id_ultimo_produto_cadastrado, equal_to(id_produto_cadastrado))