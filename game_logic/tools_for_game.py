from urllib.request import urlopen
from bs4 import BeautifulSoup
from random import randint, choice
from time import sleep


def definir_jogador_da_vez(lista_de_jogadores, jogadores_jogaram=None):
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


def sem_acentos(palavra_com_acentos):
    palavra_sem_acentos = palavra_com_acentos.replace('í', 'i').replace('é', 'e').replace('ã', 'a').replace(' ', '')
    palavra_sem_acentos = palavra_sem_acentos.replace('á', 'a').replace('ó', 'o').replace('õ', 'o').replace('ú', 'u')
    palavra_sem_acentos = palavra_sem_acentos.replace('â', 'a').replace('ô', 'o').replace('ê', 'e').replace('ç', 'c')
    return palavra_sem_acentos.upper()


def escolhe_palavra_pc():
    print('A vez é do PC, ele escolherá uma palavra agora.')
    lista = []
    if not lista:
        html = urlopen("https://www.vortexmag.net/as-73-palavras-mais-usadas-na-lingua-portuguesa/")
        bsObj = BeautifulSoup(html.read(), "html.parser")
        listas_de_palavras = bsObj.findAll("ul")
        for lista_de_palavra in listas_de_palavras:
            if '<ul>' in str(lista_de_palavra):
                palavras = lista_de_palavra.findAll('li')
                for palavra in palavras:
                    lista.append(palavra.get_text())
    while True:
        escolha = choice(lista)
        escolha = escolha[0:-1]
        if len(escolha) <= 2:
            continue
        if escolha[-1] in ('!', ';'):
            continue
        else:
            escolha = sem_acentos(escolha)
            break
    return escolha


def pc_escolhendo_letra(alfabeto, letras_ja_chutadas):
    print('O PC está escolhendo uma letra...')
    sleep(2)
    while True:
        letra = choice(alfabeto)
        if letra in letras_ja_chutadas:
            continue
        else:
            print(f'O PC escolheu a letra {letra}')
            return letra


def definir_pontos_adivinhou_single(jogadores, jogador_que_adivinha):
    for jogador in jogadores:
        if jogador.get('nome') == jogador_que_adivinha:
            jogador['pontos'] += 1


def definir_pontos_nao_adivinhou_single(jogadores, jogador_formulou_palavra):
    for jogador in jogadores:
        if jogador.get('nome') == jogador_formulou_palavra:
            jogador['pontos'] += 1


if __name__ == '__main__':
    print(escolhe_palavra_pc())
