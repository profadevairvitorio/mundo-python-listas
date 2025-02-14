# 24. Você está viajando para outro país e precisa converter a hora local.
# Peça um horário no formato 24h e adicione 5 horas para simular o fuso horário.

hora = int(input("Digite a hora (formato 24h): "))

minuto = int(input("Digite os minutos: "))

# Ajustando a hora com 5 horas de diferença
hora_convertida = (hora + 5) % 24

print(f"A hora convertida é {hora_convertida}:{minuto:02d}")