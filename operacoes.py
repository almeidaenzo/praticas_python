#Exercício 3 - Operações Matemáticas
"""
Crie um programa que:

> Peça dois números inteiros ao usuário.
> Mostre a soma, a subtração, a multiplicação e a divisão entre eles.
"""

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
