from user_interactions.for_user_interaction import *
from game_logic.tools_for_game import *
from show_for_user.shows import *

jogadores_ja_jogaram_na_rodada_da_bateria = []
jogadores_ja_colocaram_a_palavra = []
letras_adivinhadas = []
letras_chutadas = []
erros_na_palavra = 0
inicio_bateria = True
palavra_certa = None
comeca_bateria = None

inicio_mostrar()
tipo_jogo = definindo_tipo_jogo()
if tipo_jogo == '2':
    jogadores = definir_jogadores(definir_quantidade_jogadores())
    print()
    mostrar_jogadores(jogadores)
    print()
    while True:
        while inicio_bateria:
            if len(jogadores_ja_colocaram_a_palavra) == len(jogadores):
                jogadores_ja_colocaram_a_palavra.clear()
            comeca_bateria = definir_jogador_da_vez(jogadores)
            if comeca_bateria in jogadores_ja_colocaram_a_palavra:
                continue
            else:
                palavra_certa = recebendo_palavra_usuario(comeca_bateria)
                jogadores_ja_colocaram_a_palavra.append(comeca_bateria)
                jogadores_ja_jogaram_na_rodada_da_bateria.clear()
                letras_adivinhadas.clear()
                letras_chutadas.clear()
                erros_na_palavra = 0
                jogadores_ja_jogaram_na_rodada_da_bateria.append(comeca_bateria)
                inicio_bateria = False
                break
        mostrar_forca_palavra(palavra_certa, letras_adivinhadas, erros_na_palavra)
        if len(jogadores_ja_jogaram_na_rodada_da_bateria) == len(jogadores):
            jogadores_ja_jogaram_na_rodada_da_bateria.clear()
            jogadores_ja_jogaram_na_rodada_da_bateria.append(comeca_bateria)
        jogador_vez = definir_jogador_da_vez(jogadores, jogadores_ja_jogaram_na_rodada_da_bateria)
        jogadores_ja_jogaram_na_rodada_da_bateria.append(jogador_vez)
        letra_da_vez = receber_letra(jogador_vez, letras_chutadas)
        letras_chutadas.append(letra_da_vez)
        if letra_da_vez in palavra_certa:
            letras_adivinhadas.append(letra_da_vez)
        else:
            erros_na_palavra += 1
        resultado = definir_se_ganhou_perdeu(palavra_certa, erros_na_palavra, letras_adivinhadas, jogador_vez)
        if resultado == 'NAO_ADIVINHOU':
            definir_pontos_nao_adivinhou(jogadores, comeca_bateria)
            inicio_bateria = True
        elif resultado == 'ADIVINHOU':
            definir_pontos_adivinhou(jogadores, comeca_bateria, jogador_vez)
            inicio_bateria = True
