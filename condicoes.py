#Exercício 4 - Condições (if/else)
"""
Crie um programa que:

> Pergunte a idade do usuário.
> Mostre uma mensagem dizendo se ele é maior de idade (18 anos ou mais) ou menor de idade.
"""

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
    