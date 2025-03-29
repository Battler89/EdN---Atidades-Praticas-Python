# Programa para verificar se o ano é bissexto
ano = int(input("Digite o ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é um ano bissexto.")
else:
     print(f"O ano {ano} não é um ano bissexto.")
