from datetime import datetime

# Formatando uma data
data_hora_atual = datetime.now()
mascara_ptbt = '%d/%m/%Y %H'
data_hora_atual_formatada = data_hora_atual.strftime(mascara_ptbt)
print(data_hora_atual_formatada)

# Convertendo uma data
data_hora_string = '2023-10-20 10:20'
mascara_en = "%Y-%m-%d %H:%M"
data_hora_string_convertida = datetime.strptime(data_hora_string, mascara_en)
print(data_hora_string_convertida)