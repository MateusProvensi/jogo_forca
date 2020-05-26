from os import system


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
    print(
        'Olá, fico feliz que esteja jogando, vamos as regras:\n'
        'Ah, lembrando, este jogo da forca é diferente.\n\n'
        'Instruções para o single player:\n'
        'Você jogara contra o PC, ele escolherá uma palavra e você terá que adivinhar, depois, ele adivinhará sua palavra.\n'
        'Os pontos serão da seguinte forma: Quem adivinhou ganha 1 ponto. Se não for adivinhada, quem formulou a palavra ganha 1 ponto\n\n'
        'Instruções para o multiplayer:\n'
        'Será feito em baterias e dentro dessas baterias haverão rodadas,\n'
        'Vocês terão que contar com a sorte e pensando no futuro pois\n'
        'Cada um terá uma tentativa por rodada, porém a ordem de cada rodada será aleatória\n'
        'Os pontos serão da seguinte forma:\n'
        'Quem adivinha a palavra ganha 2 pontos, o restante ganha 1 e quem formulou a palavra não ganha nada\n'
        'Quando ela não for adivinhada, quem a formulou ganha 2 pontos e o restante não ganha nada'
    )
    input('\nPressione enter para continuar')



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
    print(f'O placar está da seguinte forma:\n')
    for jogador in lista_jogadores:
        print(f'Jogador(a): {jogador.get("nome")}; Pontos: {jogador.get("pontos")};')


def limpa_tela():
    system('cls')


if __name__ == '__main__':
    instrucoes()
