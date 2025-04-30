def pares(limite):
    lista = []
    i = 2  #mudei aqui
    while i <= limite:  #mudei aqui
        lista.append(i)
        i = i+2         #mudei aqui
    return lista

a = pares(15)
assert (a == [2,4,6,8,10,12,14])
a = pares(10)
assert (a == [2,4,6,8,10])
a = pares(3)
assert (a == [2])