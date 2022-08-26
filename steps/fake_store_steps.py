from pages.fake_store_page import fakeStorePage
from behave import step


@step(u'que eu acesso a API de Produtos')
def step_impl(context):
     pass


@step(u'eu consulto todos os produtos')
def step_impl(context):
     fakeStorePage.consultar_produtos(context)


@step(u'devo visualizar o status code <status_code>')
def step_impl(context):
     fakeStorePage.validar_status_code(context, context.table[0]["status_code"])


@step(u'validar a quantidade de produtos igual a <quantidade_produto>')
def step_impl(context):
     fakeStorePage.validar_quantidade_produtos(context, context.table[0]["quantidade_produto"])


@step(u'validar o produto "{nome_produto}" com o valor "{valor_produto}"')
def step_impl(context, nome_produto, valor_produto):
     fakeStorePage.validar_dados_produtos(context, nome_produto, valor_produto)


@step(u'eu realizo o cadastro de um produto')
def step_impl(context):
    fakeStorePage.cadastro_produtos(context)


@step(u'validar o dado do produto cadastro')
def step_impl(context):
     tipo_dado_produto = context.table.headings[0]  
     fakeStorePage.validar_produtos_cadastrados(context, tipo_dado_produto)


@step(u'validar o id do produto')
def step_impl(context):
     fakeStorePage.validar_id_produto(context)
