def calculadora(num1, num2, operador): 
    if operador == "+":
        resultado = num1 + num2
        #print(f"Você escolheu adição o resultado vai ser{resultado}")
        return resultado
    elif operador == "-":
        resultado = num1 - num2
        #print(f"Você escolheu subtração o resultado vai ser {resultado}")
        return resultado 
    elif operador == "/":
        resultado = num1 / num2
        #print(f"Você escolheu divisão o resultado vai ser {resultado}")
        return resultado
    elif operador == "*": 
        resultado = num1 * num2
        #print(f"Você escolheu multiplicação o resultado vai ser {resultado}")
        return resultado
    else:
        print("Resultado invalido.")

assert calculadora(5, 3, '+') == 8
assert calculadora(10, 4, '-') == 6
assert calculadora(6, 3, '*') == 18
assert calculadora(15, 3, '/') == 5

#num1 = int(input("Insira o primeiro número: "))
#num2  = int(input("Insira o segundo número: "))
#operador = input("Escolha um operador (+, -, /, *): ")
#calculadora(num1, num2, operador)
