from game_logic.tools_for_game import *


def definir_jogadores(quantidade_jogadores):
    print()
    jogadores = []
    for jogador in range(1, quantidade_jogadores + 1):
        jogador_atual = {
            'nome': '',
            'pontos': 0,
        }
        while len(jogador_atual.get('nome')) <= 3:
            jogador_atual['nome'] = input(f'Digite o seu nome, player {jogador}: ')
            if len(jogador_atual.get('nome')) <= 3:
                print('O seu nome deve ter mais que 3 caracteres.')
        jogadores.append(jogador_atual)
    jogador_atual = {
        'nome': '',
        'pontos': 0,
    }
    if quantidade_jogadores == 1:
        jogador_atual['nome'] = 'PC'
        jogadores.append(jogador_atual)
    return jogadores


def definir_quantidade_jogadores():
    while True:
        print()
        try:
            quantidade = int(input('Digite a quantidade de jogadores, máximo de 5: '))
        except TypeError:
            print('Digite um número válido')
            continue
        except ValueError:
            print('Digite um número válido')
            continue
        if quantidade > 5:
            print('O máximo de jogadores é 5, desculpe.')
        elif quantidade < 2:
            print('É multiplos jogadores, então, 2 ou mais.')
        else:
            return quantidade


def definindo_tipo_jogo():
    while True:
        print()
        print('-=' * 25)
        print(
            'Escolha o modo de jogo:\n'
            '1 - Singleplayer\n'
            '2 - Multiplos jogadores\n'
            '3 - Instruções'
        )
        print('-=' * 25)
        escolha_tipo_jogo = input('Digite a sua escolha: ')
        if escolha_tipo_jogo in ('1', '2', '3'):
            return escolha_tipo_jogo
        else:
            print('Escolha uma opção válida.')


def recebendo_palavra_usuario(usuario_vez):
    print(f'É a hora do jogador(a) {usuario_vez}, lembrando que letras com acentos serão realocados para sem acentos e '
          f'cedilhas para a letra c')
    while True:
        palavra = input('\nDigite a palavra que será adivinhada: ')
        if len(palavra) < 2:
            print('Sua palavra deve ter 2 caracteres ou mais.')
        elif palavra.isalpha():
            palavra = palavra.lower()
            return sem_acentos(palavra)
        elif palavra.isalnum() or palavra.isnumeric():
            print('Sua palavra deve ser constituida apenas por letras.')


def sem_acentos(palavra_com_acentos):
    palavra_sem_acentos = palavra_com_acentos.replace('í', 'i').replace('é', 'e').replace('ã', 'a').replace(' ', '')
    palavra_sem_acentos = palavra_sem_acentos.replace('á', 'a').replace('ó', 'o').replace('õ', 'o').replace('ú', 'u')
    palavra_sem_acentos = palavra_sem_acentos.replace('â', 'a').replace('ô', 'o').replace('ê', 'e').replace('ç', 'c')
    return palavra_sem_acentos.upper()


def receber_letra(jogador_vez, letras_ja_digitadas, palavra_certa, erros):
    letras_impossiveis = ('/', '*', '-', '+', '´', '`', '^', '~', ',', '.', ';', ':', '[', ']', '{', '}', '\'', '\"',
                          '<', '>')
    while True:
        print()
        letra = input(f'Digite uma letra, {jogador_vez}[& para chutar]: ')
        if letra == '&':
            while True:
                palavra_chute = input('\nDigite a palavra que você acha que é: ')
                if palavra_chute == '':
                    print('Não pode ser vazio.')
                else:
                    palavra_chute = palavra_chute.upper()
                    palavra_chute_lista = list(palavra_chute)
                    resultado_do_chute = definir_se_ganhou_perdeu(palavra_certa, erros, palavra_chute_lista,
                                                                  jogador_vez)
                    return resultado_do_chute
        if len(letra) > 1 or len(letra) < 1:
            print('A letra é apenas um caractere.')
            continue
        elif letra.isnumeric():
            print('Precisamos de uma letra e não um número.')
            continue
        elif letra in letras_impossiveis:
            print('Esta letra é impossível.')
            continue
        letra = letra.upper()
        if letra in letras_ja_digitadas:
            print('Esta letra já foi digitada.')
            continue
        else:
            return letra


def continuar_jogar():
    while True:
        continuar = input('\nDeseja continuar a jogar[S/N]? ')
        if continuar not in ('S', 'N', 's', 'n'):
            print('Digite S ou N.')
            continue
        else:
            continuar = continuar.upper()
            if continuar == 'S':
                return True
            elif continuar == 'N':
                return False


if __name__ == '__main__':
    resultado = receber_letra('Mateus', ['a', 'v', 'q'], 'BOLO', 3)
    print(resultado)
    pass
