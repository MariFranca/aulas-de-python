ano = int(input("Insira o ano: "))
if ano % 4 == 0:
    print("Ano da olimpiada.")
elif ano % 4 == 2: 
    copa = True
elif not olimpiada and not copa:
    print("nada aconteceu esse ano")
else:
    print("aconteceu um evento esse ano")