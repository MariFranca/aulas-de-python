#faça uma funcao que recebe 3 numeros, e retorna True se eles estão em ordem crescente, 
#False se não estao. Se houver numeros repetidos, retorne False
def ordemCrescente(num1, num2, num3):
    if num1 <num2 > num3:
        return True
    elif num3 > num2 > num1:
        return False
    else:
        print("Não pode haver números repetidos. ") 

assert ordemCrescente(1, 2, 3) == True
assert ordemCrescente(3, 2, 1) == False
assert ordemCrescente(-1, 0, 1) == True
assert ordemCrescente(1, 1, 2) == False
