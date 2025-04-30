def numero(lista, elemento):
    for numero_lista in lista:
        if elemento == numero_lista:
            return True
    return False
    

assert(numero([11,22,33,44],33) == True)
assert(numero([11,22,33,44],50) == False)
assert(numero([44],44) == True)
assert(numero([],44) == False)