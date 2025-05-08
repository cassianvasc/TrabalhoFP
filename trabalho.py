import os
os.system("cls")

def adicionar_animal():
    informações = []
    nome = input("Escreva o nome do animal: ")
    informações.append(input(f"Escreva a espécie de {nome}: "))
    informações.append(input(f"Escreva a raça de {nome}: "))
    informações.append(input(f"Escreva a data de nascimento de {nome}: "))
    informações.append(input(f"Escreva o peso de {nome}: "))
    pets[nome] = informações
    file = open("file.txt", "w", encoding='utf8')
    file.write(str(pets)+"\n")
    file.close()
    return pets


def visualizar_animal(nome):
    print(f"Nome: {nome}")
    print(f"Espécie: {pets[nome][0]}")
    print(f"Raça: {pets[nome][1]}")
    print(f"Data de nascimento: {pets[nome][2]}")
    print(f"Peso: {pets[nome][3]}")


def editar_animal(nome):
    pets[nome][0] = input("Escreva a nova espécie: ")
    pets[nome][1] = input("Escreva a nova raça: ")
    pets[nome][2] = input("Escreva a nova data de nascimento: ")
    pets[nome][3] = input("Escreva o novo peso: ")
    

def excluir_animal(nome):
    del pets[nome]


def registrar_evento():
    compromisso = []
    print("Qual evento você deseja registrar?")
    opcao = int(input("1- Vacinações, 2- Consultas Veterinárias, 3- Aplicações de remédios\n"))

    if opcao < 1 or opcao > 3:
        while opcao < 1 or opcao > 3:
            opcao = int(input("Opção inválida. Escolha uma das opções citadas: "))

    if opcao == 1:
        compromisso.append(nomeErrado(input("Você quer marcar a vacinação para que pet? ")))
        compromisso.append(input("Para que dia você quer marcar a sua vacinação? (dd/mm/aaaa) "))
        compromisso.append(input("Alguma observação em relação á vaincação? "))
        eventos['vacinas'].append(compromisso)
        
        
    elif opcao == 2:
        compromisso.append(nomeErrado(input("Você quer marcar a consulta para que pet? ")))
        compromisso.append(input("Para que dia você quer marcar a sua consulta? (dd/mm/aaaa) "))
        compromisso.append(input("Alguma observação em relação á consulta? "))
        eventos['consultas'].append(compromisso)
        
    else:
        compromisso.append(nomeErrado(input("Você quer marcar a aplicação de remédios para que pet? ")))
        compromisso.append(input("Para que dia você quer marcar a sua aplicações? (dd/mm/aaaa) "))
        compromisso.append(input("Alguma observação em relação a aplicação de remédiosw? "))
        eventos['remedios'].append(compromisso)
        
    compromisso = []


def nomeErrado(nome):
    while nome not in pets:
        nome = input("Esse pet não foi cadastrado. Escreva outro nome: ")
    return nome

pets = {}
eventos = {'vacinas': [], 'consultas': [], 'remedios': []}
nome = ''
opcao = 0

while True:
    print("O que você deseja fazer?")
    opcao = int(input("1- Adicionar um pet, 2- Visualizar um pet, 3- Editar um pet ja existente, 4- Excluir um pet, 5- Registrar eventos, 6- Sair\n"))
    
    if opcao == 1:
        adicionar_animal()
        print("Pet adicionado.")
    elif opcao == 2:
        nome = input("Qual o nome do animal que você deseja visualizar? ")
        visualizar_animal(nomeErrado(nome))
        print("Itens visualizados.")
    elif opcao == 3:
        nome = input("Qual o nome do animal que você deseja editar? ")
        editar_animal(nomeErrado(nome))
        print("Itens alterados.")
    elif opcao == 4:
        nome = input("Qual o nome do animal que você deseja remover? ")
        excluir_animal(nomeErrado(nome))
        print("Itens removidos.")
    elif opcao == 5:
        registrar_evento
    elif opcao == 6:
        break
    else:
        while opcao < 1 or opcao > 5:
            opcao = int(input("Opção inválida. Digite uma opção dentro das disponíveis: "))
        

