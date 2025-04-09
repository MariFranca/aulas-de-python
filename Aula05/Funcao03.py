def calculando(velocidade, kilometragemAtual ):
    resultado = velocidade * 2
    kilometragem = resultado + kilometragemAtual
    print(f"A velocidade após duas horas é {kilometragem}")
    return kilometragem

velocidade = int(input("Insira a velocidade em km/h: "))
kilometragemAtual = 250 
calculando(velocidade, kilometragemAtual)