                                        # Desafio 1 — Calculadora de Troco

# Você foi ao mercado e comprou alguns produtos.
# O programa deve:
# 1 - Perguntar o valor total da compra.
# 2 - Perguntar o valor pago pelo cliente.
# 3 - Calcular o troco e mostrar uma mensagem formatada


valor_compra = float(input("Digite o valor da compra: "))
valor_pago = float(input("Digite o valor pago: "))


print(f"Valor da compra: {valor_compra:.2f}")
print(f"Valor pago: {valor_pago:.2f}")

if valor_pago < valor_compra:
    print("Valor insuficiente para pagar a compra!")
else:
    troco = valor_pago - valor_compra
    print(f"Valor do troco: {troco:.2f}")
