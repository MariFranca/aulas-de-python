minuto_inicil = int(input("Insira os minutos:"))
minutos_que_passaram = int(input("Insira os minutos que passaram:"))

calculo = (minuto_inicil + minutos_que_passaram)%60
calculo_2 = (minuto_inicil + minutos_que_passaram)//60 
print("se passaram", calculo)
print("As horas são,", calculo_2)
