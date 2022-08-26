from pages.fake_store_pages import FakeApi
from behave import given, when, then
from hamcrest import assert_that, equal_to
from json import loads


@given(u'que eu acesso a API de Produtos')
def step_impl(context):
     FakeApi.consultar_produto(context)
     FakeApi.criar_produto(context)


@when(u'eu realizo o cadastro')
def step_impl(context):
     print("Teste 2")


@then(u'devo visualizar o status code 200')
def step_impl(context):
     print("Teste 3")


@then(u'o id do produto cadastrado')
def step_impl(context):
     print("Teste 4")