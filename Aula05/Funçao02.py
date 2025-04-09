#Escreva uma função que recebe o ano de nascimento da pessoa e 
#retorna a idade atual da pessoa (em 2025)

def CalculaIdade(ano, nome):
    resultado = 2025 - ano
    return resultado

a = CalculaIdade(2007, "Breno")
print(f"Você tem {a}")
b = CalculaIdade(2020, "Flavia")
print(f"Você tem {b}")
c = CalculaIdade(2001, "Guilherme")
print(f"Você tem {c}")

#ano = int(input("Insira seu ano de nascimento: "))
#CalculaIdade(ano)