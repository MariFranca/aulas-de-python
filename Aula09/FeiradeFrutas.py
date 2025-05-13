def preco_feira(frutas: list[str]) -> float:
    valor = 0
    for item in frutas:
    
        if item == 'banana':
            valor += 1.50
        elif item == 'abacate':
            valor += 4.99
        elif item == 'tomate':
            valor += 3.25 
    return valor
            

            

        
        
       



# Testes
assert preco_feira(['banana']) != None, "Sua funcao retornou None. Isso quer dizer que você esqueceu o return"
assert preco_feira(['banana']) == 1.50, "Uma banana deve custar R$ 1.50"
assert preco_feira(['abacate', 'tomate']) == 8.24, "Abacate + tomate deve custar R$ 8.24"
assert preco_feira(['banana', 'banana']) == 3.00, "Duas bananas dá 3 reais"
assert preco_feira([]) == 0, "Lista vazia dá 0"

print("todos os testes passaram!")
print("E se fossem 50 tipos de frutas diferentes? No semestre que vem, vamos refazer essa funcao, usando dicionarios")
#Banana: R$ 1,50
#Abacate: R$ 4,99
#Tomate: R$ 3,25
