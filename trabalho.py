import os
os.system("cls")

def adicionar_animal(nome,especie, raca, datanascimento, peso ):
    informacoes= f"{nome};{especie};{raca};{datanascimento};{peso}"
    return informacoes


def salvar_arquivo(filename, informacoes):
    file = open(filename, "a", encoding='utf8') # lembrar de limpar os files antes de enviar
    file.writelines(informacoes + "\n")
    file.close()


# def visualizar_animal():
#     with open ("file.txt", "r", encoding="utf8") as file:
#         for linha in file:
#             animais = linha.strip().split(";")
#             print(f"Nome: {animais[0]}; Espécie: {animais[1]}; raça: {animais[2]}; Data de nascimento: {animais[3]}; peso: {animais[4]}")

def visualizar_animal(nome_pet):
    encontrado = False

    with open("file.txt", "r", encoding="utf8") as file:
        for linha in file:
            dados = linha.strip().split(";")
            if dados[0].lower() == nome_pet.lower():
                print(f"Nome: {dados[0]}")
                print(f"Espécie: {dados[1]}")
                print(f"Raça: {dados[2]}")
                print(f"Data de nascimento: {dados[3]}")
                print(f"Peso: {dados[4]}")
                encontrado = True
                break

    if not encontrado:
        print(f"Pet com nome '{nome_pet}' não encontrado.")


# def editar_animal():
#     editar=input("Digite o nome do animal que você quer editar: ")
#     encontrado = False
#     with open("file.txt", "r", encoding="utf8") as file:
#         linhas = file.readlines()
#     with open("file.txt", "w", encoding="utf8") as file:
#         for linha in linhas:
#             animais = linha.strip().split(";")
#             if animais[0] == editar:
#                 nome=  input("Escreva o nome do novo animal: ")
#                 especie = input(f"Digite a especie de {nome} ")
#                 raca = input(f"Digite a raça de {nome} ")
#                 datanascimento = input(f"Digite a data de nascimento de {nome} ")
#                 peso = input(f"Digite o peso de {nome} ")
#                 novalinha = f"{nome};{especie};{raca};{datanascimento};{peso}\n"
#                 file.write(novalinha)
#                 encontrado = True
#             else:
#                 file.write(linha)
#         if not encontrado:
#             print("Animal nao encontrado")
#         else:
#             print("Animal editado com sucesso")

def editar_animal():
    editar = input("Digite o nome do animal que você quer editar: ")
    encontrado = False

    with open("file.txt", "r", encoding="utf8") as file:
        linhas = file.readlines()

    with open("file.txt", "r+", encoding="utf8") as file: # r+ permite que o código seja lido e editado
        for linha in linhas:
            animais = linha.strip().split(";")
            if len(animais) < 5:
                file.write(linha)  # pula linhas mal formatadas (elementos faltando)
                continue

            if animais[0].lower() == editar.lower():
                nome = input("Escreva o nome do novo animal: ")
                especie = input(f"Digite a espécie de {nome}: ")
                raca = input(f"Digite a raça de {nome}: ")
                datanascimento = input(f"Digite a data de nascimento de {nome}: ")
                peso = input(f"Digite o peso de {nome}: ")
                nova_linha = f"{nome};{especie};{raca};{datanascimento};{peso}\n"
                file.write(nova_linha)
                encontrado = True
            else:
                file.write(linha) # manter iguais linhas que não foram editadas

    if encontrado:
        print("Animal editado com sucesso.")
    else:
        print("Animal não encontrado.")
    

def excluir_animal(): 
    excluir = input("Digite o nome do animal que você quer excluir: ")
    encontrado = False

    with open("file.txt", 'r', encoding="utf-8") as file:
        linhas = file.readlines()

    with open("file.txt", 'w', encoding="utf-8") as file:
        for linha in linhas:
            animal = linha.strip().split(";")
            if animal[0] == excluir:
                encontrado = True
                continue
            else:
                file.write(linha)
        if not encontrado:
            print("Animal não encontrado.")
        else:
            print("Animal excluido com sucesso.")
   

def registrar_evento():
    print("Qual evento você deseja registrar?")
    opcao = int(input("1- Vacinações, 2- Consultas Veterinárias, 3- Aplicações de remédios\n"))

    if opcao < 1 or opcao > 3:
        while opcao < 1 or opcao > 3:
            opcao = int(input("Opção inválida. Escolha uma das opções citadas: "))

    if opcao == 1:
        nome = input("Você quer marcar a vacinação para que pet? ")

        # Verificar se o pet existe no arquivo file.txt
        pet_encontrado = False
        with open("file.txt", "r", encoding="utf8") as file:
            for linha in file:
                dados = linha.strip().split(";")
                if dados and dados[0].lower() == nome.lower():
                    pet_encontrado = True
                    break

        if pet_encontrado:
            data_vacinacao = input("Para que dia você quer marcar a vacinação? (dd/mm/aaaa) ")
            observacao = input("Alguma observação em relação à vacinação? ")

            # Salva o compromisso no arquivo vacinas.txt
            with open("vacinas.txt", "a", encoding="utf8") as file:
                file.write(f"Pet: {nome}\n")
                file.write(f"Data da vacinação: {data_vacinacao}\n")
                file.write(f"Observações: {observacao}\n\n")

            print(f"Vacinação marcada com sucesso para o pet {nome}.")
        else:
            print(f"O pet '{nome}' não foi encontrado no registro. Por favor, registre o pet primeiro.")
    
    #     #compromisso.append(nomeErrado(input("Você quer marcar a vacinação para que pet? ")))
    #     nome = input("Você quer marcar a vacinação para que pet? ")
    #     compromisso.append(nome)
    #     compromisso.append(input("Para que dia você quer marcar a sua vacinação? (dd/mm/aaaa) "))
    #     compromisso.append(input("Alguma observação em relação á vaincação? "))
    #     eventos['vacinas'].append(compromisso)
    #     file = open("vacinas.txt", "a", encoding='utf8')
    #     file.writelines(eventos['vacinas'][nome])
    #     file.close()
        
        
    elif opcao == 2:
        nome = input("Você quer marcar a consulta para que pet? ")

        # Verificar se o pet existe no arquivo file.txt
        pet_encontrado = False
        with open("file.txt", "r", encoding="utf8") as file:
            for linha in file:
                dados = linha.strip().split(";")
                if dados and dados[0].lower() == nome.lower():
                    pet_encontrado = True
                    break

        if pet_encontrado:
            data_consulta = input("Para que dia você quer marcar a consulta? (dd/mm/aaaa) ")
            observacao = input("Alguma observação em relação à consulta? ")

            # Salva o compromisso no arquivo vacinas.txt
            with open("consultas.txt", "a", encoding="utf8") as file:
                file.write(f"Pet: {nome}\n")
                file.write(f"Data da consulta: {data_consulta}\n")
                file.write(f"Observações: {observacao}\n\n")

            print(f"Consulta marcada com sucesso para o pet {nome}.")
        else:
            print(f"O pet '{nome}' não foi encontrado no registro. Por favor, registre o pet primeiro.")

        # compromisso.append(nomeErrado(input("Você quer marcar a consulta para que pet? ")))
        # compromisso.append(input("Você quer marcar a consulta para que pet? "))
        # compromisso.append(input("Para que dia você quer marcar a sua consulta? (dd/mm/aaaa) "))
        # compromisso.append(input("Alguma observação em relação á consulta? "))
        # eventos['consultas'].append(compromisso)
        # file = open("consultas.txt", "a", encoding='utf8')
        # file.writelines("")
        # file.close()
        
    else:
        nome = input("Você quer marcar a aplicação para que pet? ")

        # Verificar se o pet existe no arquivo file.txt
        pet_encontrado = False
        with open("file.txt", "r", encoding="utf8") as file:
            for linha in file:
                dados = linha.strip().split(";")
                if dados and dados[0].lower() == nome.lower():
                    pet_encontrado = True
                    break

        if pet_encontrado:
            data_aplicacao = input("Para que dia você quer marcar a aplicação? (dd/mm/aaaa) ")
            observacao = input("Alguma observação em relação à aplicação? ")

            # Salva o compromisso no arquivo vacinas.txt
            with open("aplicacoes.txt", "a", encoding="utf8") as file:
                file.write(f"Pet: {nome}\n")
                file.write(f"Data da aplicacao: {data_aplicacao}\n")
                file.write(f"Observações: {observacao}\n\n")

            print(f"Aplicação marcada com sucesso para o pet {nome}.")
        else:
            print(f"O pet '{nome}' não foi encontrado no registro. Por favor, registre o pet primeiro.")

        # compromisso.append(nomeErrado(input("Você quer marcar a aplicação de remédios para que pet? ")))
        # compromisso.append(input("Você quer marcar a aplicação de remédios para que pet? "))
        # compromisso.append(input("Para que dia você quer marcar a sua aplicações? (dd/mm/aaaa) "))
        # compromisso.append(input("Alguma observação em relação a aplicação de remédiosw? "))
        # eventos['remedios'].append(compromisso)
        # file = open("aplicacoes.txt", "a", encoding='utf8')
        # file.writelines("")
        # file.close()
        


# def nomeErrado(nome):
#     while nome not in pets:
#         nome = input("Esse pet não foi cadastrado. Escreva outro nome: ")
#     return nome

pets = {}
eventos = {'vacinas': [], 'consultas': [], 'remedios': []}
nome = ''
opcao = 0

while True:
    print("O que você deseja fazer?")
    opcao = int(input("1- Adicionar um pet, 2- Visualizar um pet, 3- Editar um pet ja existente, 4- Excluir um pet, 5- Registrar eventos, 6- Sair\n"))
    
    if opcao == 1:      
        nome = input("Digite o nome do animal: ")
        especie = input(f"Digite a especie de {nome}: ")
        raca = input(f"Digite a raça de {nome}: ")
        datanasc = input(f"Digite a data de nascimento de {nome}: ")
        peso =input (f"Digite o peso de {nome}: ")
        infos = adicionar_animal(nome, especie, raca, datanasc, peso ) 
        salvar_arquivo("file.txt", infos)
        print("Pet adicionado.")

    elif opcao == 2:
        nome = input("Qual o nome do animal que você deseja visualizar? ")
        visualizar_animal(nome) 
        
    elif opcao == 3:
        editar_animal()
        
    elif opcao == 4:
        excluir_animal()

    elif opcao == 5:
        registrar_evento()
        
    elif opcao == 6:
        break
    else:
        while opcao < 1 or opcao > 5:
            opcao = int(input("Opção inválida. Digite uma opção dentro das disponíveis: "))
        

