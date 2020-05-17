def definir_jogador_da_vez(lista_de_jogadores, jogadores_jogaram=None):
    from random import randint
    if jogadores_jogaram is None:
        jogadores_jogaram = []
    while True:
        jogador_escolhido = randint(0, len(lista_de_jogadores) - 1)
        if lista_de_jogadores[jogador_escolhido].get('nome') in jogadores_jogaram:
            continue
        else:
            jogador_escolhido = lista_de_jogadores[jogador_escolhido].get('nome')
            return jogador_escolhido


def definir_se_ganhou_perdeu(palavra_certa, erros, letras_adivinhadas, jogador_vez):
    print()
    if set(sorted(palavra_certa)) == set(sorted(letras_adivinhadas)):
        print(f'Parabéns, o vencedor desta bateria foi o(a) {jogador_vez}')
        print(f'A palavra correta era: {palavra_certa}')
        print()
        return 'ADIVINHOU'
    elif erros == 9:
        print(f'Ninguém adivinhou a palavra.')
        print(f'A palavra correta era: {palavra_certa}')
        print()
        return 'NAO_ADIVINHOU'
    else:
        return None



def definir_pontos_nao_adivinhou(lista_jogadores, formulador_questao):
    for jogador in lista_jogadores:
        if jogador.get('nome') == formulador_questao:
            jogador['pontos'] += 2


def definir_pontos_adivinhou(lista_jogadores, formulador_questao, jogador_vez):
    for jogador in lista_jogadores:
        if jogador.get('nome') == formulador_questao:
            jogador['pontos'] += 0
        elif jogador.get('nome') == jogador_vez:
            jogador['pontos'] += 2
        else:
            jogador['pontos'] += 1
