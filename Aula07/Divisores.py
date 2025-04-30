def divisores(num):
    lista = []
    i = 1
    while i <= num:
        if num % i == 0:
            lista.append(i)
        i + 1
    return lista

a = divisores(15)
assert(a == [1,3,5,15])

b = divisores(16)
assert(b == [1,2,4,8,16])