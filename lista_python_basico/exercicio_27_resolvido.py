# 27. Você precisa saber que dia da semana será daqui a "X" dias.
# Peça ao usuário um número e exiba o dia correspondente.
import datetime

dias = int(input("Digite o número de dias: "))

hoje = datetime.datetime.now()
# Calculando o dia da semana após X dias

novo_dia = hoje + datetime.timedelta(days=dias)

print(f"Daqui a {dias} dias será {novo_dia.strftime('%A')}.")
