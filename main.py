"""
    Módulo principal para a aplicação Controle de Estoque Unifecaf.
    Este módulo serve como ponto de entrada para a aplicação, inicializando
    e gerenciando as funcionalidades principais do sistema de controle de estoque.
    Criado por: Jonathan Yuri
    github: https://github.com/jonathan-JIPSlok
"""
# Importing the necessary modules
import os

# modulo que contem a interface de opções do sistema.
from system_interface import user_options, cabecalho
from system_options import adicionar_items
from system_options import update_product, list_items, remove_product
from system_options.data_manipuling import DataManipuling

# Cria o diretório data com 'os.mkdir' caso ele não exista que é verificado por 'os.path.exists'
os.mkdir('data') if not os.path.exists('data') else None

# Constants
DATA_FILE_INVENTORY = 'data/inventory.json' # Define o caminho do arquivo de dados do iventário.
DATA_FILE_CLIENTS = 'data/clients.json' # Define o caminho do arquivo de dados dos clientes.
DATA_FILE_SALES = 'data/sales.json' # Define o caminho do arquivo de dados das vendas.
SYSTEM_OPTIONS = ('Registrar vendas', 'Adicionar Cliente', 'Visualizar Vendas','Adicionar Produto', 'Atualizar Produto', 'Remover Produto', 'Listar Produtos', 'Listar Clientes') # Define as opções do sistema
DATA_PRODUCTS = DataManipuling(DATA_FILE_INVENTORY).get_data() # Dicionario que armazena os produtos do inventário
DATA_CLIENTS = DataManipuling(DATA_FILE_CLIENTS).get_data() # Dicionario que armazena os clientes
DATA_SALES = DataManipuling(DATA_FILE_SALES).get_data() # Dicionario que armazena as vendas

user = ""
while user != "sair":
    cabecalho()

    user = user_options(SYSTEM_OPTIONS)
    if user == 'sair':
        print('Saindo do Sistema...')
        break
    elif user == '0':
        adicionar_items(DATA_SALES).sales(DATA_PRODUCTS, DATA_CLIENTS)
        DataManipuling(DATA_FILE_SALES).save_data(DATA_SALES) # Salva os dados das vendas no arquivo
        DataManipuling(DATA_FILE_INVENTORY).save_data(DATA_PRODUCTS) # Salva os dados do inventário no arquivo
    elif user == '1':
        adicionar_items(DATA_CLIENTS).clients() # Adiciona um cliente ao sistema
        DataManipuling(DATA_FILE_CLIENTS).save_data(DATA_CLIENTS) # Salva os dados dos clientes no arquivo
    elif user == '2':
        cabecalho("Vendas Realizadas")
        list_items(DATA_SALES, True, 'vendas') # Lista as vendas realizadas
    elif user == '3':
        adicionar_items(DATA_PRODUCTS).product() # Adiciona um produto ao inventário
        DataManipuling(DATA_FILE_INVENTORY).save_data(DATA_PRODUCTS) # Salva os dados do inventário no arquivo
    elif user == '4':
        update_product(DATA_PRODUCTS) # Atualiza um produto do inventário
        DataManipuling(DATA_FILE_INVENTORY).save_data(DATA_PRODUCTS) # Salva os dados do inventário no arquivo
    elif user == '5':
        remove_product(DATA_PRODUCTS) # Remove um produto do inventário
        DataManipuling(DATA_FILE_INVENTORY).save_data(DATA_PRODUCTS) # Salva os dados do inventário no arquivo
    elif user == '6':
        cabecalho("Produtos em Estoque")
        list_items(DATA_PRODUCTS, True) # Lista os produtos do inventário detalhadamente
    elif user == '7':
        cabecalho("Clientes Cadastrados")
        list_items(DATA_CLIENTS, detalhado=True, tipo='clientes') # Lista os clientes cadastrados
    
    else: # Caso o usuário digite uma opção não disponível.
        print('Opção inválida! Tente novamente.')
        continue