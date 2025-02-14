# 21. Um prédio inteligente ajusta a quantidade de peso que pode suportar com base na média de peso dos passageiros.
# Peça o peso de três pessoas e exiba o peso médio delas.

peso1 = float(input("Digite o peso da primeira pessoa: "))

peso2 = float(input("Digite o peso da segunda pessoa: "))

peso3 = float(input("Digite o peso da terceira pessoa: "))

# Calculando o peso médio
media_peso = (peso1 + peso2 + peso3) / 3

print("Peso médio:", media_peso)
