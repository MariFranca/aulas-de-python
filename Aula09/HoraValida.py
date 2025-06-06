def eh_hora_valida(horas: int, minutos: int) -> bool:
    if horas <= 24 and  minutos <=59:
        return True
    elif horas > 24 and minutos > 59:
        return False

# Testes
assert eh_hora_valida(12, 30) != None, "Sua funcao retornou None. Isso quer dizer que você esqueceu o return"
assert eh_hora_valida(12, 30) == True, "Meio dia e meia era para ser valido"
assert eh_hora_valida(0, 0) == True, "Meia-noite deve ser valida"
assert eh_hora_valida(23, 59) == True, "Ultimo minuto do dia deve ser valido"
assert eh_hora_valida(24, 0) == True, "Consideramos que ambos 24:00 e 00:00 sao o mesmo horario"
assert eh_hora_valida(12, 60) == False, "Minutos inválidos (maior que 59)"
assert eh_hora_valida(25, 60) == False, "Minutos inválidos (maior que 59)"
assert eh_hora_valida(25, 12) == False, "Minutos inválidos (maior que 59)"
print("Todos os testes passaram!")