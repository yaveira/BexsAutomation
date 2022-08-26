from pages.fake_store_pages import FakeApi
from behave import given, when, then, step
from hamcrest import assert_that, equal_to
from json import loads


@step(u'que eu acesso a API de Produtos')
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


@step(u'validar o produto "{nome_produto}" com o valor "{valor_produto}"')
def step_impl(context, nome_produto, valor_produto):
     lista_produtos = loads(context.lista_produtos.text)

     if len(lista_produtos) >= 1:
          for i in range(len(lista_produtos)):
               if lista_produtos[i]['title'] == nome_produto and lista_produtos[i]['price'] == float(valor_produto):
                    assert_that(nome_produto, equal_to(lista_produtos[i]['title']))
                    assert_that(float(valor_produto), equal_to(lista_produtos[i]['price']))
     else:
          raise AssertionError('Name and value is not present')


@step(u'eu realizo o cadastro de um produto')
def step_impl(context):
    context.lista_produtos = FakeApi.criar_produto(context)


@then(u'validar o "title" do produto cadastro')
def step_impl(context):
    assert_that(context.table[0]['title'], equal_to(context._root['active_outline'][0]))


@then(u'validar o "price" do produto cadastro')
def step_impl(context):
    assert_that(context.table[0]['price'], equal_to(context._root['active_outline'][1]))


@then(u'validar o "description" do produto cadastro')
def step_impl(context):
    assert_that(context.table[0]['description'], equal_to(context._root['active_outline'][2]))


@then(u'validar o "image" do produto cadastro')
def step_impl(context):
    assert_that(context.table[0]['image'], equal_to(context._root['active_outline'][3]))


@then(u'validar o "category" do produto cadastro')
def step_impl(context):
    assert_that(context.table[0]['category'], equal_to(context._root['active_outline'][4]))


@step(u'validar o id do produto')
def step_impl(context):
     lista_produtos = loads(context.lista_produtos.text)
     quantidade_itens_na_lista = len(loads(FakeApi.consultar_produto(context).text)) + 1

     assert_that(quantidade_itens_na_lista, equal_to(lista_produtos['id']))
