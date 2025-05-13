def digito_ou_letra(caractere):
    digito = ''
    if caractere digito.isalpha():
        print("letra")
    elif caractere digito.isdigit():
        print("digito")


assert digito_ou_letra('a') != None, "sua funcao retornou None. Isso significa que você esqueceu de dar return"
assert digito_ou_letra('a') == 'letra'
assert digito_ou_letra('z') == 'letra'
assert digito_ou_letra('3') == 'digito'
assert digito_ou_letra('@') == 'nenhum'