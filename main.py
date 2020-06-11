from user_interactions.for_user_interaction import *
from game_logic.tools_for_game import *
from show_for_user.shows import *

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
jogadores_ja_jogaram_na_rodada_da_bateria = []
jogadores_ja_colocaram_a_palavra = []
letras_adivinhadas = []
letras_chutadas = []
erros_na_palavra = 0
inicio_bateria = True
palavra_certa = None
comeca_bateria = None
jogador_que_adivinha = None
tentou_adivinhar_palavra = False
resultado = ''

inicio_mostrar()
while True:
    tipo_jogo = definindo_tipo_jogo()
    limpa_tela()
    if tipo_jogo == '1':
        jogadores = definir_jogadores(1)
        while True:
            while inicio_bateria:
                if len(jogadores) == len(jogadores_ja_colocaram_a_palavra):
                    jogadores_ja_colocaram_a_palavra.clear()
                comeca_bateria = definir_jogador_da_vez(jogadores)
                if comeca_bateria in jogadores_ja_colocaram_a_palavra:
                    continue
                else:
                    if comeca_bateria == 'PC':
                        palavra_certa = escolhe_palavra_pc()
                        jogador_que_adivinha = jogadores[0].get('nome')
                    else:
                        print()
                        palavra_certa = recebendo_palavra_usuario(comeca_bateria)
                        jogador_que_adivinha = 'PC'
                    jogadores_ja_colocaram_a_palavra.append(comeca_bateria)
                    letras_adivinhadas.clear()
                    letras_chutadas.clear()
                    erros_na_palavra = 0
                    inicio_bateria = False
            limpa_tela()
            mostrar_forca_palavra(palavra_certa, letras_adivinhadas, erros_na_palavra)
            if jogador_que_adivinha == 'PC':
                letra_da_vez = pc_escolhendo_letra(alfabeto, letras_chutadas)
            else:
                letra_da_vez = receber_letra(jogadores[0].get('nome'), letras_chutadas, palavra_certa, erros_na_palavra)
            if letra_da_vez == 'ADIVINHOU':
                tentou_adivinhar_palavra = True
                resultado = 'ADIVINHOU'
            elif letra_da_vez is None:
                tentou_adivinhar_palavra = True
                resultado = None
                print('Que pena, você errou :(, mas o jogo continua.')
                sleep(1.5)
            if not tentou_adivinhar_palavra:
                letras_chutadas.append(letra_da_vez)
                if letra_da_vez in palavra_certa:
                    if jogador_que_adivinha == 'PC':
                        print('O PC acertou uma letra.')
                    else:
                        print('Você acertou uma letra.')
                    sleep(1)
                    letras_adivinhadas.append(letra_da_vez)
                else:
                    if jogador_que_adivinha == 'PC':
                        print('O PC errou.')
                    else:
                        print('Você errou.')
                    sleep(1)
                    erros_na_palavra += 1
                resultado = definir_se_ganhou_perdeu(palavra_certa, erros_na_palavra, letras_adivinhadas,
                                                     jogador_que_adivinha)
            if resultado == 'NAO_ADIVINHOU':
                definir_pontos_nao_adivinhou_single(jogadores, comeca_bateria)
                print()
                mostrar_placar(jogadores)
                print()
                inicio_bateria = True
            elif resultado == 'ADIVINHOU':
                definir_pontos_adivinhou_single(jogadores, jogador_que_adivinha)
                print()
                mostrar_placar(jogadores)
                print()
                inicio_bateria = True
            if inicio_bateria:
                continuar_jogo = continuar_jogar()
                if not continuar_jogo:
                    print('\nPor que nos abandonou? :(\n')
                    mostrar_placar(jogadores)
                    input('\nPressione enter para confirmar sua saída')
                    exit()
                limpa_tela()

    if tipo_jogo == '2':
        jogadores = definir_jogadores(definir_quantidade_jogadores())
        limpa_tela()
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
            limpa_tela()
            mostrar_forca_palavra(palavra_certa, letras_adivinhadas, erros_na_palavra)
            if len(jogadores_ja_jogaram_na_rodada_da_bateria) == len(jogadores):
                jogadores_ja_jogaram_na_rodada_da_bateria.clear()
                jogadores_ja_jogaram_na_rodada_da_bateria.append(comeca_bateria)
            jogador_vez = definir_jogador_da_vez(jogadores, jogadores_ja_jogaram_na_rodada_da_bateria)
            jogadores_ja_jogaram_na_rodada_da_bateria.append(jogador_vez)
            letra_da_vez = receber_letra(jogador_vez, letras_chutadas, palavra_certa, erros_na_palavra)
            if letra_da_vez == 'ADIVINHOU':
                tentou_adivinhar_palavra = True
                resultado = 'ADIVINHOU'
            elif letra_da_vez is None:
                tentou_adivinhar_palavra = True
                resultado = None
                print('Que pena, você errou :(, mas o jogo continua.')
                sleep(2)
            if not tentou_adivinhar_palavra:
                letras_chutadas.append(letra_da_vez)
                if letra_da_vez in palavra_certa:
                    letras_adivinhadas.append(letra_da_vez)
                else:
                    erros_na_palavra += 1
                resultado = definir_se_ganhou_perdeu(palavra_certa, erros_na_palavra, letras_adivinhadas, jogador_vez)
            if resultado == 'NAO_ADIVINHOU':
                definir_pontos_nao_adivinhou(jogadores, comeca_bateria)
                print()
                mostrar_placar(jogadores)
                print()
                inicio_bateria = True
            elif resultado == 'ADIVINHOU':
                definir_pontos_adivinhou(jogadores, comeca_bateria, jogador_vez)
                print()
                mostrar_placar(jogadores)
                print()
                inicio_bateria = True
            if inicio_bateria:
                continuar_jogo = continuar_jogar()
                if not continuar_jogo:
                    print('\nPor que nos abandonou? :(\n')
                    mostrar_placar(jogadores)
                    input('\nPressione enter para confirmar sua saída')
                    exit()
                limpa_tela()
    elif tipo_jogo == '3':
        print()
        instrucoes()
