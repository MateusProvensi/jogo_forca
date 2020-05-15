def inicio_mostrar():
    print('-=' * 25)
    print('Bem vindo ao seu jogo da forca'.center(50))
    print('-=' * 25)


def mostrar_jogadores(lista_de_jogadores):
    print('Os jogadores são: ', end='')
    jogador_numero = 1
    for jogador in lista_de_jogadores:
        if jogador_numero == len(lista_de_jogadores) - 1:
            print(jogador.get('nome'), end=' e ')
        elif jogador_numero == len(lista_de_jogadores):
            print(jogador.get('nome'))
        else:
            print(jogador.get('nome'), end=', ')
        jogador_numero += 1


def instrucoes():
    pass


def mostrar_forca_palavra(palavra_certa, letras_adivinhadas, erros):
    print()
    forca = ['''
_______
|/      |
|
|
|
|
|
|___''', '''
_______
|/      |
|       0
|
|
|
|
|___''', '''
_______
|/      |
|       0
|       |
|
|
|
|___''', '''
_______
|/      |
|       0
|       |
|       |
|
|
|___''', '''
_______
|/      |
|       0
|       |\\
|       |
|
|
|___''', '''
_______
|/      |
|       0
|      /|\\
|       |
|
|
|___''', '''
_______
|/      |
|       0
|      /|\\
|       |
|        \\
|
|___''', '''
_______
|/      |
|       0
|      /|\\
|       |
|      / \\
|
|___''', '''
_______
|/      |
|       0
|      /|\\
|       |
|      / \\_ 
|
|___''', '''
_______
|/      |
|       0
|      /|\\
|       |
|    _/  \\_ 
|
|___'''
             ]
    print(forca[erros])
    print()
    for caractere in palavra_certa:
        if caractere in letras_adivinhadas:
            print(caractere, end=' ')
        else:
            print('_', end=' ')
    print()


def mostrar_placar(lista_jogadores):
    pass
