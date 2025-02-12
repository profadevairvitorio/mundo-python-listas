# Solicite duas notas (números decimais) e exiba a média.

# Solicitar ao usuário a primeira nota (número decimal)
# A função input() pede ao usuário para digitar um valor.
# Esse valor será tratado como uma string, então usamos o casting (float()) para convertê-lo em número decimal.
nota1 = float(input("Digite a primeira nota: "))

# Solicitar ao usuário a segunda nota (número decimal)
# Similar à primeira nota, usamos input() e convertemos para float.
nota2 = float(input("Digite a segunda nota: "))

# Calcular a média das duas notas
# Somamos as duas notas (nota1 + nota2) e depois dividimos o resultado por 2 para encontrar a média.
media = (nota1 + nota2) / 2

# Exibir o resultado da média
# A função print() exibe a mensagem na tela.
# A variável media já contém o resultado do cálculo, e o Python converte o número decimal em uma string para exibição.
print("A média das notas é:", media)
