from os import system

from time import sleep

from system_interface import cabecalho

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
        cabecalho("Adicionar Produtos")
        product_name = input('Nome do Produto: ').lower()
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
        cabecalho("Atualizar Produtos")

        # Exibe os produtos disponíveis para atualização
        list_products(data_products)
        
        print("\n[sair] para voltar ao menu principal\n")
        user = input("Selecione o produto que deseja atualizar: ")

        try:
            if user == 'sair':
                break

            elif user.isnumeric():
                system('cls')
                produto = list(data_products.keys())[int(user)]

                # mostra o produto selecionado
                print("-" * 50)
                print(f'Produto selecionado: {produto}')
                print(f'Preço: R${data_products[produto]['Preço']:.2f}')
                print(f'Quantidade: {data_products[produto]['Quantidade']}')
                print("-" * 50)

                # menu de opções
                print("[1] - Atualizar preço do produto")
                print("[2] - Atualizar quantidade do produto")
                print("[sair] - Voltar ao menu principal\n")

                user = input("Selecione a opção desejada: ")

                if user == 'sair': break

                elif user == '1': # Atualiza o preço do produto
                    data_products[produto]['Preço'] = float(input("Digite o novo preço do produto:"))
                    print("Produto atualizado com sucesso!")
                    sleep(2)

                elif user == '2': # Atualiza a quantidade do produto
                    data_products[produto]['Quantidade'] = int(input("Digite a nova quantidade do produto:"))
                    print("Produto atualizado com sucesso!")
                    sleep(2)

                else:
                    print("Opção inválida! Tente novamente.")
                    sleep(2)

            else: # Caso o usuário digite uma opção não disponível que não seja um número.
                print("Opção inválida! Tente novamente.")
                sleep(2)
        except IndexError: # Trata o erro caso o usuário digite um número que não corresponda a nenhum produto.
            print("Opção inválida! Tente novamente.")
            sleep(2)
        except ValueError:
            print('Valor inválido! Tente novamente.')
            sleep(2)


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