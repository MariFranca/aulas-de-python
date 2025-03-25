#fazendo a raiz de uma equação como se pede o exercicio
#ax**2 + bx + c =0
a = float(input("Insira o valor de A:"))
b = float(input("Insira o valor de B:"))
c = float(input("Insira o valor de C:"))

delta = b**2 - 4 * a * c

raiz1 = (-b + delta**0.5)/(a*2)
raiz2 = (-b - delta **0.5)/(a*2)
