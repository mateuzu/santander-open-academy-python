from datetime import date, datetime, time

# 2020 = ano, 10 = mes, 1 = dia (formato yyyy/mm/dd)
data = date(2020, 10, 1)
data_atual = date.today()
print("Data qualquer ", data)
print("Data atual ", data_atual)

# 2020 = ano, 1, mes, 10 = dia, 20 = horas, 15 = minutos, 0 = segundos (formato yyyy/mm/dd HH:mm:ss)
data_hora = datetime(2020, 1, 10, 20, 15, 0)
data_hora_atual = datetime.today()
print("Data-hora qualquer ",data_hora)
print("Data-hora atual ", data_hora_atual)

#10 = horas, 30 = minutos, 45 = segundos (ainda da pra passar centésimos, milissegundos, etc)
tempo = time(10, 30, 45)
print("Tempo qualquer ",tempo)
