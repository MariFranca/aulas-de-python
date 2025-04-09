#Função que retorna a média 
#ver se alguma altura é maior que 2.5 e menor que 0.5

def altura(A1, A2, A3):
    if A1 > 2.5 or A2 > 2.5 or A3 > 2.5:
        print("Essa altura é invlida.")
        return False
    elif A1 < 0.5 or A2 < 0.5 or A3 < 0.5:
        print("Essa altura é invalida.")
        return False
    else:
        return True 
def media(A1, A2, A3):
    return (A1 + A2 + A3)/3
    
altura1 = float(input("Insira a primeira altura: "))
altura2 = float(input("Insira a segunda altura: "))
altura3 = float(input("Insira a terceira altura: "))
alturaValida = altura(altura1, altura2, altura3)