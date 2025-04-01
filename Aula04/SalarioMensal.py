salario_mensal = int(input("Insira seu salario mensal: "))
salario_anual = 33888
paga_imposto =  (salario_mensal*12)

if paga_imposto <= salario_anual:
    print("Você não presisa pagar imposto.")
else:
    print("Você precisa pagar imposto. ")
