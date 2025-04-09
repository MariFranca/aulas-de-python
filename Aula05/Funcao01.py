
def PodeVotar(nome, idade):
    if idade >= 16:
        print(f"Sim,{nome} você pode votar.")
        return True
    else:
        print(f"Não, {nome} você não pode voltar.")
        return False

a = PodeVotar("Valentina", 30)
print(f"A primeira resposta é {a}")
b = PodeVotar("Pedro", 12)
print(f"A segunda resposta é {b}")
c = PodeVotar("Camila", 50 )
print(f"A terceira resposta é {c}")

#nome = input("Insira o seu nome: ")
#idade = int(input("Insira sua idade:"))
#PodeVotar(nome, idade)