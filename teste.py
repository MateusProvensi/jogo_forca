from urllib.request import urlopen
from bs4 import BeautifulSoup
import random

lista = []


def escolhe():
    if not lista:
        html = urlopen("https://www.vortexmag.net/as-73-palavras-mais-usadas-na-lingua-portuguesa/")
        bsObj = BeautifulSoup(html.read(), "html.parser")
        nameList = bsObj.findAll("ul")
        for name in nameList:
            if '<ul>' in str(name):
                lista.append(name.find('li').get_text())
    escolha = random.choice(lista)
    escolha = escolha[0:-1]
    return escolha.upper()
    # return lista


print(escolhe())
