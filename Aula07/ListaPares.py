def pares(lista):
    lista_numeros = []
    for num in lista:
        if num % 2 == 0:
            lista_numeros.append(num)
    return lista_numeros

assert(pares([11,22,33,44]) == [22,44])
assert(pares([11,33,55]) == [])
assert(pares([11,33,50,60]) == [50,60])