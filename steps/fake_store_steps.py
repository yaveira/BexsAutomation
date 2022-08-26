from pages.fake_store_pages import FakeApi
from behave import given, when, then, step
from hamcrest import assert_that, equal_to
from json import loads


@step(u'que eu acesso a API de Produtos')
def step_impl(context):
     pass


@step(u'eu realizo o cadastro')
def step_impl(context):
     FakeApi.criar_produto(context)


@step(u'devo visualizar o status code 200')
def step_impl(context):
     pass


@step(u'o id do produto cadastrado')
def step_impl(context):
     pass


@step(u'eu consulto todos os produtos')
def step_impl(context):
     context.lista_produtos = FakeApi.consultar_produto(context)


@step(u'devo visualizar o status code <status_code>')
def step_impl(context):
     status_code = context.table[0]["status_code"]
     assert_that(status_code, equal_to(str(context.lista_produtos.status_code)))


@step(u'validar a quantidade de produtos igual a <quantidade_produto>')
def step_impl(context):
     quantidade_produto = context.table[0]["quantidade_produto"]
     assert_that(quantidade_produto, equal_to(str(len(loads(context.lista_produtos.text)))))


@step(u'validar o produto SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s com o valor Value 2')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then validar o produto SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s com o valor Value 2')