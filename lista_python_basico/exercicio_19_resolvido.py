# 19. Verifique se um número é primo.
num = int(input("Digite um número: "))

# Verificando se o número é primo
if num < 2:
    print("Não é primo.")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Não é primo.")
            break
    else:
        print("É primo.")
