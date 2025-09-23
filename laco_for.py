#Exercício 5 - Laços de repetição
"""
Crie um programa que:

> Peça um número inteiro ao usuário.
> Mostre a tabuada desse número de 1 a 10.

"""

numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
