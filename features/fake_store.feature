# Created by yaveira at 25/08/2022

Feature: Product manager

@test @wip
Scenario: Consultar produto
    Given que eu acesso a API de Produtos
    When eu realizo o cadastro
    Then devo visualizar o status code 200
    And o id do produto cadastrado


@test
Scenario: Criar produto
    Given que eu acesso a API de Produtos
    When eu realizo o cadastro
    Then devo visualizar o status code 200
    And o id do produto cadastrado