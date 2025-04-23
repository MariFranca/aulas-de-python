def pode_aposentar(sexo, contribuicao, idade):
    if sexo == "feminino" and andcontribuicao >= 15 and idade >= 62:
        print("Pode aposentar!")
        return True
    elif sexo == "feminino" and andcontribuicao < 15 or idade < 62:
        print("Não pode aposentar! ")
        return False
    elif sexo == "masculino" and andcontribuicao >= 15 and idade >= 65:
        print("Pode aposentar!")
        return True 
    elif sexo == "masculino" and andcontribuicao < 15 or idade < 65:
        print("Não pode aposentar!")
        return False
    else:
        print("Não se aplica nos padroes")

sexo = input("Insira o seu sexo: ")
contribuicao = input("Insira quantos anos de contribuição você possui: ")
idade = int(input("Insira a sua idade: "))
pode_aposentar(sexo, contribuicao, idade)
