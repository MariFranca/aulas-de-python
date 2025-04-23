def pares(lista):
    nova_lista = []
    for numero in lista:
        if numero % 2 == 0:
            print(numero)
        nova_lista.append(numero) 



assert(pares([11,22,33,44]) == [22, 44])
assert(pares([11,33,55]) == [])
assert(pares([11,33,50,60]) == [50,60])