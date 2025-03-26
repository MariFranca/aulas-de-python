nota = float(input("Insira a sua nota: "))
presenca = int(input("Insira sua presença: "))

if (presenca >= 75) and (nota >= 6):
    print("Aprovado")
elif (nota <= 4) or (presenca <= 40):
    print("Você está de exame.")
else:
    print("Você está reprovado")
#ou 
aprovado =    (nota >= 6) and (presenca >= 75)
reprovado =    (nota < 4)  or  (presenca < 75)
exame =    (nota >= 4) and (nota < 6) and (presenca >= 75)
exame =    (     4 <= nota < 6      ) and (presenca >= 75)
exame =    (not aprovado) and (not reprovado)


