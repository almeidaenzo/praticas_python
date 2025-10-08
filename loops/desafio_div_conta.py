# Você e seus amigos foram a um restaurante e querem dividir a conta igualmente.
# O programa deve:
# 1 - Pedir o valor total da conta.
# 2 - Perguntar quantas pessoas vão dividir.
# 3 - Calcular e mostrar quanto cada pessoa deve pagar.


valor_conta = float(input("Digite o valor total da conta:   "))
pessoas = int(input("Quantas pessoas irão dividir a conta?  "))
gorjeta = input("Deseja incluir os 10% do garçom?   (s/n)").lower()

if pessoas < 1:
    print("Não é possível dividir, pois o número de pessoas é menor que 1!")

elif gorjeta == "s":
    gorjeta = (valor_conta * 0.1)
    print(f"Valor total da conta: R${valor_conta:.2f}")
    print(f"Número de pessoas: {pessoas}")
    print(f"Cada pessoa deve pagar: R${valor_conta / pessoas:.2f}")
    print(f"Valor da taxa de serviço do garçom: R${gorjeta:.2f}")
    if pessoas == 1:
        print(f"Apenas uma pessoa irá pagar, não é necessário dividir a conta!")
else:
    print(f"Cada pessoa deve pagar: {valor_conta / pessoas:.2f}")




#programa ajustado com algumas correções

valor_conta = float(input("Digite o valor total da conta: "))
pessoas = int(input("Quantas pessoas irão dividir a conta? "))
gorjeta = input("Deseja incluir os 10% do garçom? (s/n): ").lower()

if pessoas < 1:
    print("❌ Não é possível dividir, pois o número de pessoas é menor que 1!")
else:
    if gorjeta == "s":
        valor_total = valor_conta * 1.1  # adiciona 10%
        print(f"\n💰 Valor total com 10%: R$ {valor_total:.2f}")
    else:
        valor_total = valor_conta
        print(f"\n💰 Valor total sem gorjeta: R$ {valor_total:.2f}")

    if pessoas == 1:
        print("⚠️ Apenas uma pessoa irá pagar a conta inteira!")
        print(f"Valor a pagar: R$ {valor_total:.2f}")
    else:
        valor_por_pessoa = valor_total / pessoas
        print(f"👥 Cada pessoa deve pagar: R$ {valor_por_pessoa:.2f}")

