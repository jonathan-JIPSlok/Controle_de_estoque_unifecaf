""""
    Main module for the Controle de Estoque Unifecaf application.
    This module serves as the entry point for the application, initializing
    and managing the core functionalities of the inventory control system.
    Created by: Jonathan Yuri
    github: https://github.com/jonathan-JIPSlok
"""
# Importing the necessary modules
import os

# modulo que contem a interface de opções do sistema.
from system_interface import user_options, cabecalho
from system_options import add_product, update_product, list_products, remove_product
from system_options.data_manipuling import get_data, save_data

# Cria o diretório data com 'os.mkdir' caso ele não exista que é verificado por 'os.path.exists'
os.mkdir('data') if not os.path.exists('data') else None

# Constants
DATA_FILE = 'data/inventory.json' # Define o caminho do arquivo de dados do iventário.
SYSTEM_OPTIONS = ('Registrar vendas', 'Adicionar Produto', 'Atualizar Produto', 'Remover Produto', 'Listar Produtos') # Define as opções do sistema
DATA_PRODUCTS = get_data(DATA_FILE) # Dicionario que armazena os produtos do inventário

user = ""
while user != "sair":
    cabecalho()

    user = user_options(SYSTEM_OPTIONS)
    if user == 'sair':
        save_data(DATA_FILE, DATA_PRODUCTS) # Salva os dados do inventário no arquivo
        print('Saindo do Sistema...')
        break
    elif user == '0':
        pass
    elif user == '1':
        add_product(DATA_PRODUCTS) # Adiciona um produto ao inventário
    elif user == '2':
        update_product(DATA_PRODUCTS) # Atualiza um produto do inventário
    elif user == '3':
        remove_product(DATA_PRODUCTS) # Remove um produto do inventário
    elif user == '4':
        cabecalho("Produtos em Estoque")
        list_products(DATA_PRODUCTS, True) # Lista os produtos do inventário detalhadamente
    
    else: # Caso o usuário digite uma opção não disponível.
        print('Opção inválida! Tente novamente.')
        continue