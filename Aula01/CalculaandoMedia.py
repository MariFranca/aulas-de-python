N1 = int(input("Insira sua primeira nota: "))
N2 = int(input("Insira sua segunda nota: "))
N3 = int(input("Insira sua terceira nota: "))

soma = N1+N2+N3
media = soma/3

if media >= 7:
    print("Você está aprovado.")
else:
    print("Você não foi aprovado.")