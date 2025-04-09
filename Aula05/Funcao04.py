def telefone(quantidadeCaracteres):
    if quantidadeCaracteres == 8:
        print(f"{numeroTelefone} esse númro é válido, e é um telefone fixo.")
    elif quantidadeCaracteres == 9:
        print(f"{numeroTelefone} esse número é válido, e é um número de celular. ")
    elif quantidadeCaracteres == 10:
        print(f"{numeroTelefone} esse número é válido, é telefone fixo com ddd. ")
    else:
        print("Esse número não é valido.") 

numeroTelefone = input("Insira o seu telefone: ")
quantidadeCaracteres = len(numeroTelefone)
telefone(quantidadeCaracteres)
