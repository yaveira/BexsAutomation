# Created by yaveira at 25/08/2022

Feature: Product manager

Background: Background name
    Given que eu acesso a API de Produtos

@test @wip
Scenario Outline: Consultar produtos
    When eu consulto todos os produtos
    Then devo visualizar o status code <status_code>
        | status_code |
        | 200         |
    And validar a quantidade de produtos igual a <quantidade_produto>
        | quantidade_produto |
        | 20                 |
    And validar o produto <nome_produto> com o valor <valor_produto>

    Examples:
        | nome_produto                                          | valor_produto |
        | SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s   | Value 2       |


@test
Scenario: Criar produto
    When eu realizo o cadastro
    Then devo visualizar o status code 200
    And o id do produto cadastrado