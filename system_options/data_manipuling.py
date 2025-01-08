import os

import json
from time import sleep

class DataManipuling:
    def __init__(self, data_file: str):
        self.data_file = data_file
        pass

    def get_data(self) -> dict:
        """
        Carrega os dados de um arquivo .json.
        :param file: Caminho do arquivo.
        :return: Dados do arquivo.
        """
        try:
            # Tenta abrir o arquivo e carregar os dados
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            return {}
    
    def save_data(self, data: dict) -> None:
        """
        Salva os dados em um arquivo .json.
        :param file: Caminho do arquivo.
        :param data: Dados a serem salvos.
        """
        # salva os dados no arquivo
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)
        
        print('Dados salvos com sucesso!')
        sleep(1)