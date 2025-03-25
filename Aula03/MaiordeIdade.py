idade = int(input("Insira sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menos de idade.")

#jeito feito pelo professor
idade = int(input("Insira sua idade:"))
maior_de_idade = idade >= 18
menos_de_idade = idade < 18
menos_de_idade = not maior_de_idade