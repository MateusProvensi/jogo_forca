from urllib.request import urlopen
from bs4 import BeautifulSoup
import random

lista = []


def escolhe():
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
        escolha = random.choice(lista)
        escolha = escolha[0:-1]
        if len(escolha) <= 2:
            continue
        else:
            break
    return escolha.upper()
    #return lista


print(escolhe())
