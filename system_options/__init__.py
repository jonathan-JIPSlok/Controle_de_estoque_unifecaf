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

        if not product_name in data_products.keys(): # Verifica se o produto já existe no inventário
            
            #Adiciona o produto ao dicionário de produtos
            data_products[product_name] = {'Preço': product_price, 'Quantidade': product_quantity}
            print("Produto adicionado com sucesso!")
            sleep(2)
        
        else:
            print("Produto já existe no inventário!")
            sleep(2)
    
    except ValueError: #Trata o erro caso o usuário digite um valor inválido como palavras em vez de números
        print('Valor inválido! Tente novamente.')
        sleep(2)

def update_product(data_products: dict) -> None:
    """
    Atualiza um produto do inventário.
    """
    user = ''
    while user != 'sair':
        print('Produtos disponiveis para atualização:')

        # Exibe os produtos disponíveis para atualização
        list_products(data_products)
        
        print("[sair] para voltar ao menu principal")
        user = input("Selecione o produto que deseja atualizar: ")


def remove_product(data_products: dict) -> None:
    """
    Remove um produto do inventário.
    """
    pass

def list_products(data_products: dict) -> None:
    """
    Lista os produtos do inventário.
    """
    # Exibe os produtos disponíveis no inventário
    for indice, product in enumerate(data_products.keys()):
        print(f'[{indice}] - {product}')