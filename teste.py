lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listar_iter = iter(lista)

while True:
    proximo = next(listar_iter, 'ACABOU')
    if proximo == 'ACABOU':
        listar_iter = iter(lista)
        continue
    print(proximo)
