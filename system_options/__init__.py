from os import system

from time import sleep

from system_interface import cabecalho

class adicionar_items:
    def __init__(self, Data) -> None:
        """
        Adiciona um produto, um cliente ou uma venda ao sistema.
        :param Data: Dicionário que armazena os dados.
        """
        self.data = Data
    
    def product(self) -> None:
        """
        Adiciona um produto ao inventário.
        """
        try:
            cabecalho("Adicionar Produtos")
            product_name = input('Nome do Produto: ').lower().strip() # Converte o nome do produto para minúsculo e remove os espaços em branco
            product_price = float(input('Preço do Produto: ').replace(',', '.')) # Substitui a vírgula por ponto caso o usuário digite , ao invés de .
            product_quantity = int(input('Quantidade do Produto: '))

            if not product_name in self.data.keys(): # Verifica se o produto já existe no inventário
                
                #Adiciona o produto ao dicionário de produtos
                self.data[product_name] = {'Preco': product_price, 'Quantidade': product_quantity}
                print("Produto adicionado com sucesso!")
                sleep(1)
            
            else:
                print("Produto já existe no inventário!")
                sleep(1)
        
        except ValueError: #Trata o erro caso o usuário digite um valor inválido como palavras em vez de números
            print('Valor inválido! Tente novamente.')
            sleep(1)

    def clients(self):
        """
        Adicona um cliente ao sistema.
        """
        try:
            cabecalho("Adicionar Cliente")
            client_name = input('Nome Completo do Cliente: ').lower().strip() # Converte o nome do cliente para minúsculo e remove os espaços em branco
            client_cpf = input('CPF do Cliente: ').replace('.', '').replace('-', '') # Remove os pontos e traços do CPF
            client_email = input('E-mail do Cliente: ').lower().strip() # Converte o e-mail do cliente para minúsculo e remove os espaços em branco

            if not client_name in self.data.keys(): # Verifica se o cliente já existe no sistema
                # adiciona o cliente ao dicionário de clientes
                self.data[client_name] = {'CPF': client_cpf, 'Email': client_email}
                print("Cliente adicionado com sucesso!")
                sleep(1)
            
            else:
                print("Cliente já existe no sistema!")
                sleep(1)
        except:
            print('Valor inválido! Tente novamente.')
            sleep(1)

    def sales(self, data_products: dict, data_clients: dict) -> None:
        """
        Adiciona uma venda ao sistema.
        """
        produtos = []
        try:
            cabecalho("Registrar Vendas")
            list_items(data_clients) # Exibe os clientes disponíveis para a venda
            client_name = input('Nome do Cliente: ').lower().strip() # Converte o nome do cliente para minúsculo e remove os espaços em branco
            if client_name not in data_clients.keys(): # Verifica se o cliente existe no sistema
                print("Cliente não encontrado!")
                sleep(2)
                return
            user = ''
            while user != 'sair':
                cabecalho("produtos disponíveis")
                list_items(data_products) # Exibe os produtos disponíveis para a venda
                print("\n[confirmar] para concluir a venda\n")
                try:
                    # Exibe o total da venda até o momento
                    soma = 0
                    for produto in produtos:
                        soma += list(produto.values())[0]['Total']

                    print(f"Total até agora: R${soma:.2f}\n")
                    
                    #Usuario seleciona o produto e a quantidade para a venda
                    user = input("digite o número do produto: ").strip().lower()
                    if user == 'confirmar': #verifica se o usuário deseja confirmar a venda
                        break
                    else:
                        user = int(user)
                    # pede a quantidade do produto.
                    product_quantity = int(input('Quantidade do Produto: '))

                     # Verifica se a quantidade do produto é suficiente para a venda
                    if product_quantity <= data_products[list(data_products.keys())[user]]['Quantidade']:
                        product_name = list(data_products.keys())[user]
                        product_price = data_products[product_name]['Preco']
                        product_total = product_price * product_quantity

                        # Registra a saida de produtos do inventário
                        data_products[product_name]['Quantidade'] -= product_quantity

                        #Registra a venda no dicionário de vendas
                        produtos.append({product_name: {'Quantidade': product_quantity, 'Total': product_total}})
                        print(f"Produto registrado!")
                        sleep(1)
                    else:
                        print("Quantidade insuficiente para a venda!")
                        sleep(1)
                except ValueError:
                    print('Valor inválido! Tente novamente.')
                    sleep(1)
                except IndexError:
                    print('Opção inválida! Tente novamente.')
                    sleep(1)
            self.data[client_name] = produtos
        except Exception as e:
            print(f'Erro: {e}')
            sleep(1)

def update_product(data_products: dict) -> None:
    """
    Atualiza um produto do inventário.
    :param data_products: Dicionário que armazena os produtos do inventário.
    """
    user = ''
    while user != 'sair':
        cabecalho("Atualizar Produtos")

        # Exibe os produtos disponíveis para atualização
        list_items(data_products)
        
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
                print(f'Preço: R${data_products[produto]['Preco']:.2f}')
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
                    sleep(1)

                elif user == '2': # Atualiza a quantidade do produto
                    data_products[produto]['Quantidade'] = int(input("Digite a nova quantidade do produto:"))
                    print("Produto atualizado com sucesso!")
                    sleep(1)

                else:
                    print("Opção inválida! Tente novamente.")
                    sleep(1)

            else: # Caso o usuário digite uma opção não disponível que não seja um número.
                print("Opção inválida! Tente novamente.")
                sleep(1)
        except IndexError: # Trata o erro caso o usuário digite um número que não corresponda a nenhum produto.
            print("Opção inválida! Tente novamente.")
            sleep(1)
        except ValueError:
            print('Valor inválido! Tente novamente.')
            sleep(1)


def remove_product(data_products: dict) -> None:
    """
    Remove um produto do inventário.
    :param data_products: Dicionário que armazena os produtos do inventário.
    """
    user = ''
    while user != 'sair':
        cabecalho("Remover Produtos")

        # Exibe os produtos disponíveis para remoção
        list_items(data_products)
        print("\n[sair] para voltar ao menu principal\n")

        user = input("digite o nome do produto que deseja remover: ").lower().strip()
        if user == 'sair':
            break
        elif data_products.get(user, "Produto não encontrado") == "Produto não encontrado":
            #Verifica se o produto existe no inventário
            print("Produto não encontrado!")
            sleep(1)
        else:
            # Remove o produto do inventário
            del data_products[user]
            print("Produto removido com sucesso!")
            sleep(1)

def list_items(data_items: dict, detalhado = False, tipo = 'produtos') -> None:
    """
    Lista os items.
    :param data_items: Dicionário que armazena os produtos do inventário.
    :param detalhado: Parâmetro que define se a listagem será detalhada ou não.
    """
    if detalhado == False:
        # Exibe os produtos disponíveis no inventário
        for indice, item in enumerate(data_items.keys()):
            print(f'[{indice}] - {item}')
    
    elif detalhado == True and tipo == 'produtos':
        # Exibe os produtos disponíveis no inventário detalhadamente
        for indice, product in enumerate(data_items.keys()):
            print(f'[{indice}] - {product}')
            print(f'preço do produto: R${data_items[product]["Preco"]:.2f}')
            print(f'Quantidade em estoque: {data_items[product]["Quantidade"]}')
            print('-' * 50)
            print('\n')
        input("Pressione Enter para voltar ao menu principal ...")

    elif detalhado == True and tipo == 'clientes':
        # Exibe os clientes disponíveis no sistema detalhadamente
        for indice, client in enumerate(data_items.keys()):
            print(f'[{indice}] - {client}')
            print(f'CPF: {data_items[client]["CPF"]}')
            print(f'E-mail: {data_items[client]["Email"]}')
            print('-' * 50)
            print('\n')
        input("Pressione Enter para voltar ao menu principal ...")
    
    elif detalhado == True and tipo == 'vendas':
        # Exibe as vendas realizadas detalhadamente
        for client, products in data_items.items():
            print(f'Cliente: {client}')
            for product in products:
                for product_name, product_data in product.items():
                    print(f'Produto: {product_name}')
                    print(f'Quantidade: {product_data["Quantidade"]}')
                    print(f'Total: R${product_data["Total"]:.2f}')
            print('-' * 50)
            print('\n')
        input("Pressione Enter para voltar ao menu principal ...")