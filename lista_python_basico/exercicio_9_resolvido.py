# 9. Peça a idade do usuário em anos e converta para dias (desconsiderando anos bissextos).

# Solicitar a idade do usuário em anos
idade_anos = int(input("Digite sua idade em anos: "))

# Calcular a idade em dias (considerando 365 dias por ano)
idade_dias = idade_anos * 365

# Exibir o resultado
print(f"Sua idade em dias é aproximadamente: {idade_dias} dias")
