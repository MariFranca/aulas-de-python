idade = int(input("Insira sua idade: "))
if idade < 16:
    print("Você não pode.")
elif idade < 70:
    print("Você precisa votar.")
elif idade >= 16:
    print("Você pode, mas não precisa votar.")
else:
    print("Você não precisa votar.")
