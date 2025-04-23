nome = []
especie = []
raça = []
datadenascimento = []
peso = []

opcao = 0
index = 0

while True:
    print("O que você deseja fazer?")
    opcao = int(input("1- Adicionar, 2- Visualizar, 3- Editar, 4- Excluir, 5- Sair "))
    
    if opcao == 1:
        nome.append(input("Escreva o nome do animal: "))
        especie.append(input("Escreva a espécie do animal: "))
        raça.append(input("Escreva a raça do animal: "))
        datadenascimento.append(input("Escreva a data de nascimento do animal: "))
        peso.append(float(input("Escreva o peso do animal: ")))
        print("Itens adicionados.")
    elif opcao == 2:
        index = int(input("Qual o índex do animal que você deseja visualizar? "))
        print(f"Nome: {nome[index]}")
        print(f"Especie: {especie[index]}")
        print(f"Raça: {raça[index]}")
        print(f"Data de nascimento: {datadenascimento[index]}")
        print(f"Peso: {peso[index]}")
        print("Itens visualizados.")
    elif opcao == 3:
        index = int(input("Qual o índex do animal que você deseja editar? "))
        nome[index] = input("Qual será o novo nome? ")
        especie[index] = input("Qual será a nova espécie? ")
        raça[index] = input("Qual será a nova raça? ")
        datadenascimento[index] = input("Qual será a nova data de nascimento? ")
        peso[index] = float(input("Qual será o novo peso? "))
        print("Itens alterados.")
    elif opcao == 4:
        index = int(input("Qual o índice do animal que você deseja remover? "))
        del nome[index]
        del especie[index]
        del raça[index]
        del datadenascimento[index]
        del peso[index]
        print("Itens removidos.")
    elif opcao == 5:
        break
    else:
        while opcao < 1 or opcao > 5:
            opcao = int(input("Opção inválida. Digite uma opção dentro das disponíveis: "))
        