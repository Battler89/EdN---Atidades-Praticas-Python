# Programa para calcular o valor da gorjeta
def gorjeta(valor_conta, porcentagem=10):
    valor_gorjeta = (valor_conta * porcentagem) / 100
    total = valor_conta + valor_gorjeta
    return valor_gorjeta, total
conta = float(input("Digite o valor da conta: R$ "))
taxa = float(input("Digite a porcentagem da gorjeta (padrão 10%): ") or 10)
taxa_gorjeta, total_conta = gorjeta(conta, taxa)
print(f"Valor da gorjeta: R$ {taxa_gorjeta:.2f}")
print(f"Total a pagar: R$ {total_conta:.2f}")
