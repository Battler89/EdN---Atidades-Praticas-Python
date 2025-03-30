# Progrmar para identificar o total de números pares e ímpares digitados
par = 0
impar = 0
while True:
    entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")
    if entrada.lower() == "fim":
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é par.")
            par += 1
        else:
            print(f"{numero} é ímpar.")
            impar += 1
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")
print(f"Total de números pares: {par} ")
print(f"Total de números ímpares: {impar} ")
