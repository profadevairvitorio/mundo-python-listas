# 14. Exiba a data e a hora atual no formato DD/MM/AAAA HH:MM:SS. Use a biblioteca Datetime
import datetime

agora = datetime.datetime.now()

# Exibindo a data e hora atual no formato desejado
print("Data e hora:", agora.strftime("%d/%m/%Y %H:%M:%S"))