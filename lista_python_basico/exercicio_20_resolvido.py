# 20. Peça duas datas e calcule a diferença em dias entre elas.
from datetime import datetime

data1 = input("Digite a primeira data (DD/MM/AAAA): ")

data2 = input("Digite a segunda data (DD/MM/AAAA): ")

# Convertendo as strings para objetos de data
data1 = datetime.datetime.strptime(data1, "%d/%m/%Y")
data2 = datetime.datetime.strptime(data2, "%d/%m/%Y")

# Calculando a diferença em dias
diferenca = (data2 - data1).days

print("Diferença em dias:", diferenca)
