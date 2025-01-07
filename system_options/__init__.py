from time import sleep


def __init__():
    """
    Módulo que contém funções para manipular as opções do sistema.
    """
    pass

def add_product(data_products: dict) -> None:
    """
    Adiciona um produto ao inventário.
    """
    try:
        product_name = input('Nome do Produto: ')
        product_price = float(input('Preço do Produto: ').replace(',', '.')) # Substitui a vírgula por ponto caso o usuário digite , ao invés de .
        product_quantity = int(input('Quantidade do Produto: '))

        #Adiciona o produto ao dicionário de produtos
        data_products[product_name] = {'Preço': product_price, 'Quantidade': product_quantity}
        print("Produto adicionado com sucesso!")
    
    except ValueError: #Trata o erro caso o usuário digite um valor inválido como palavras em vez de números
        print('Valor inválido! Tente novamente.')
        sleep(2)