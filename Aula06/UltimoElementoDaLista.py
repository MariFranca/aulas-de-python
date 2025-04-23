def ultimo(lista):
    tamanho    = len(lista)
    ultimo_indice = tamanho - 1
    return lista[ultimo_indice]
    

lista_alunos = ["Augusto", "Pina", "Cris" ]
print(ultimo(lista_alunos))
lista_numeros = [10,20,30,40]
print(ultimo(lista_numeros))