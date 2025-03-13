divida = int(input("Insira sua divida aqui: "))
juros = 15


#primeiro mês
aumento = divida*(juros/100)
divida = divida+aumento
print("Sua divida é ",divida)

#segundo mês
aumento = divida*(juros/100)
divida = divida+aumento
print("Sua divida é ",divida)
