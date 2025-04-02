velocidade_do_carro = int(input("Insira a velocidade do carro: "))
velocidade_maxima = 40
if velocidade_do_carro > velocidade_maxima:
    print("Você tomou multa de", 130.16)
    
elif velocidade_do_carro > 1.2 * velocidade_maxima:
    print("Você tomou multa de", 195.23)
elif velocidade_do_carro > 1.5 * velocidade_maxima:
    print("Você tomou multa de", 888.41)
else:
    print("Você não tomou multa.")
    
