from os import system
from datetime import datetime # modulo que permite trabalhar com data e hora
def user_options(options: tuple) -> str:
    """
    Mostra um menu de opções para o usuário e solicita que ele selecione uma opção.
    :param options: Uma tupla contendo as opções disponíveis para o usuário.
    :return: A opção escolhida pelo usuário.
    """
    # Exibe as opções disponíveis para o usuário
    print('Selecione uma opção:\n')
    for indice, option in enumerate(options):
        print(f'[{indice}] {option}')
    print('\n[sair] Sair do Sistema\n')

    # Solicita ao usuário que selecione uma opção
    selected_option = input('Opção: ')
    
    return selected_option


def cabecalho(titulo = "Controle de Estoque") -> None:
    """
    Exibe o cabeçalho do sistema.
    """
    system('cls') # Limpa a tela do terminal
    print('-' * 70)
    print(f"\t {titulo} \t Data: {datetime.today().date()}")
    print('-' * 70)