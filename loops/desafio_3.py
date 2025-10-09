#Crie um programa que funcione como uma lista de compras simples, onde o usuário possa adicionar, visualizar e remover itens.
#Mostrar um menu de opções:

# === LISTA DE COMPRAS ===
# [1] Adicionar item
# [2] Remover item
# [3] Mostrar lista
# [4] Sair
# Enquanto o usuário não escolher “sair”, o programa deve:
# Permitir adicionar novos itens à lista;
# Permitir remover um item específico (pelo nome);
# Mostrar a lista completa sempre que for solicitado;
# Exibir uma mensagem amigável caso a lista esteja vazia.
# Tudo isso deve funcionar dentro de um loop while, com condições if/elif.

compras = []
opcao = 0

while opcao != 4:
    print()
    print("== LISTA DE COMPRAS ==")
    print("[1] Adicionar item")
    print("[2] Remover item")
    print("[3] Mostrar lista")
    print("[4] Sair")
    opcao = int(input("Digite uma opção:    "))
    print()
    if opcao == 1:
        itens = input("Adicione o item:     ").lower()
        compras.append(itens)
        print("Item adicionado com sucesso!")
    elif opcao == 2:
        if not compras:
            print("lista vazia!")
        else:
            print(compras)
            remover = input("Qual item deseja remover?  ")
            if remover in compras:
                compras.remove(remover)
                print("Item removido com sucesso!")
                print(f"Sua lista: {compras}")
            else:
                print("Item não encontrado")
    elif opcao == 3:
        if not compras:
            print("Não há itens para listar!")
        else:
            for i, item in enumerate(compras, start=1):
                print(f"{i}. {item}")
    elif opcao == 4:
        print(f"Lista encerrada\nSeus itens são: {compras}")
        

