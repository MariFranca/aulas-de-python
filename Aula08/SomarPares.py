#faça uma funcao em python que recebe um numero n e calcula
#a soma de todos os numeros de 1 ate n, mas considerando apenas os pares. Inclua o n na soma, se ele for par
def SomarPares(n):
    soma = 0 
    for numero in range(2, n +1, 2): #Começa no 2 e vai até o número que você escolheu pulando de dois em dois 
        soma += numero
    return soma 


assert SomarPares(5) == 6, f"Erro no teste 1: esperava 6 mas obteve {soma_pares(5)}"
assert SomarPares(10) == 30, f"Erro no teste 2: esperava 30 mas obteve {soma_pares(10)}"
assert SomarPares(1) == 0, f"Erro no teste 3: esperava 0 mas obteve {soma_pares(1)}"
assert SomarPares(0) == 0, f"Erro no teste 4: esperava 0 mas obteve {soma_pares(0)}"
assert SomarPares(20) == 110, f"Erro no teste 5: esperava 110 mas obteve {soma_pares(20)}"