# Programa para realizar o calculo do imc
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
resultado = peso / (altura **2)
print(f"Seu IMC é: {resultado:.2f}")
if resultado < 18.5:
    print(f"Classificação: Abaixo do peso")
elif 18.5 <= resultado < 24.9:
     print(f"Classificação: Peso normal")
elif 25 <= resultado < 29.9:
     print(f"Classificação: Sobrepeso")
else:
     print(f"Classificação: Obeso")
