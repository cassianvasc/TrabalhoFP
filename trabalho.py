import os
os.system("cls")

def adicionar_animal(nome, especie, raca, datanascimento, peso, informacoes):
    nome=input("Digite o nome do animal: ")
    especie=input(f"Digite a especie de {nome}: ")
    raca=input(f"Digite a raça de{nome}: ")
    peso=input(f"Digite o peso de{nome}: ")
    informacoes= f"{nome};{especie};{raca};{datanascimento};{peso}"
    file = open("file.txt", "a", encoding='utf8')
    file.writelines(informacoes)
    file.close()


def visualizar_animal():
    
    


def editar_animal():
    
    

def excluir_animal():
   


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
        file = open("vacinas.txt", "a", encoding='utf8')
        file.writelines("")
        file.close()
        
        
    elif opcao == 2:
        compromisso.append(nomeErrado(input("Você quer marcar a consulta para que pet? ")))
        compromisso.append(input("Para que dia você quer marcar a sua consulta? (dd/mm/aaaa) "))
        compromisso.append(input("Alguma observação em relação á consulta? "))
        eventos['consultas'].append(compromisso)
        file = open("consultas.txt", "a", encoding='utf8')
        file.writelines("")
        file.close()
        
    else:
        compromisso.append(nomeErrado(input("Você quer marcar a aplicação de remédios para que pet? ")))
        compromisso.append(input("Para que dia você quer marcar a sua aplicações? (dd/mm/aaaa) "))
        compromisso.append(input("Alguma observação em relação a aplicação de remédiosw? "))
        eventos['remedios'].append(compromisso)
        file = open("aplicacoes.txt", "a", encoding='utf8')
        file.writelines("")
        file.close()
        
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
        registrar_evento()
    elif opcao == 6:
        break
    else:
        while opcao < 1 or opcao > 5:
            opcao = int(input("Opção inválida. Digite uma opção dentro das disponíveis: "))
        

