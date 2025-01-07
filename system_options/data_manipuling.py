import os

import json
from time import sleep

def get_data(file: str) -> dict:
    """
    Carrega os dados de um arquivo .json.
    :param file: Caminho do arquivo.
    :return: Dados do arquivo.
    """
    
    try:
        # Tenta abrir o arquivo e carregar os dados
        with open(file, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return {}
    
def save_data(file: str, data: dict) -> None:
    """
    Salva os dados em um arquivo .json.
    :param file: Caminho do arquivo.
    :param data: Dados a serem salvos.
    """
    # salva os dados no arquivo
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)
    
    print('Dados salvos com sucesso!')
    sleep(1)