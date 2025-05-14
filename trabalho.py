import os
os.system("cls")

def adicionar_animal():
    # Solicita as informações ao usuário
    nome = input("Digite o nome do animal: ")
    especie = input(f"Digite a especie de {nome}: ")
    raca = input(f"Digite a raça de {nome}: ")
    datanasc = input(f"Digite a data de nascimento de {nome}: ")
    peso = input (f"Digite o peso de {nome}: ")
    # As organiza em uma string só, separada por ; para fácil edição e visualização
    informacoes = f"{nome};{especie};{raca};{datanasc};{peso}"
    # Salva as informações em "file.txt"
    with open("file.txt", "a", encoding='utf8') as file:
        file.writelines(informacoes + "\n")
    print("Pet adicionado.")


# def salvar_arquivo(filename, informacoes):  # função para salvar as informações 
#     file = open(filename, "a", encoding='utf8') # lembrar de limpar os files antes de enviar
#     file.writelines(informacoes + "\n")
#     file.close()


# def visualizar_animal():
#     with open ("file.txt", "r", encoding="utf8") as file:
#         for linha in file:
#             animais = linha.strip().split(";")
#             print(f"Nome: {animais[0]}; Espécie: {animais[1]}; raça: {animais[2]}; Data de nascimento: {animais[3]}; peso: {animais[4]}")

def visualizar_animal(nome_pet): 
    encontrado = False           

    with open("file.txt", "r", encoding="utf8") as file:
        for linha in file:
            # Transforma a linha dessa iteração em uma lista e tira espaços (tratamento de erro), salva isso em "dados"
            dados = linha.strip().split(";")
            # Checa se o primeiro elemento da lista (nome) é igual ao inserido pelo usuário
            if dados[0].lower() == nome_pet.lower():
                # Lê as informações
                print(f"Nome: {dados[0]}")
                print(f"Espécie: {dados[1]}")
                print(f"Raça: {dados[2]}")
                print(f"Data de nascimento: {dados[3]}")
                print(f"Peso: {dados[4]}")
                encontrado = True
                break
    
    # tratamento de erro caso o usuário tenha inserido um nome inválido
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
        # Guarda as linhas em uma lista, sendo cada uma um elemento
        linhas = file.readlines()

    with open("file.txt", "r+", encoding="utf8") as file: # r+ permite que o código seja lido e editado
        for linha in linhas:
            # Transforma o elemento dessa iteração (cada um é uma linha) em uma lista e tira espaços (tratamento de erro), salva isso em "animais" 
            animais = linha.strip().split(";")
            # Pula linhas mal formatas com elementos faltando (tratamento de erro)
            if len(animais) < 5:
                file.write(linha)
                continue
            
            # Checa se o primeiro elemento da lista (nome) é igual ao inserido pelo usuário
            if animais[0].lower() == editar.lower():
                # Solicita as novas informações ao usuário
                nome = input("Escreva o nome do novo animal: ")
                especie = input(f"Digite a espécie de {nome}: ")
                raca = input(f"Digite a raça de {nome}: ")
                datanascimento = input(f"Digite a data de nascimento de {nome} (dd/mm/aaaa): ")
                peso = input(f"Digite o peso de {nome}: ")
                # As organiza em uma string só, separada por ; para fácil edição e visualização
                nova_linha = f"{nome};{especie};{raca};{datanascimento};{peso}\n"
                # Salva as informações atualizadas em "file.txt"
                file.write(nova_linha)
                encontrado = True
            else:
                # Mantêm iguais linhas que não foram editadas
                file.write(linha)

    if encontrado:
        print("Animal editado com sucesso.")
    else:
        print("Animal não encontrado.")
    

def excluir_animal():
    # Solicita o nome do pet ao usuário   
    excluir = input("Digite o nome do animal que você quer excluir: ")
    encontrado = False

    with open("file.txt", 'r', encoding="utf-8") as file:
        # Guarda as linhas em uma lista, sendo cada uma um elemento
        linhas = file.readlines()

    # Arquivo aberto em modo w garante que as informações serão sobrescritas.
    with open("file.txt", 'w', encoding="utf-8") as file:
        for linha in linhas:
             # Transforma o elemento dessa iteração (cada um é uma linha) em uma lista e tira espaços (tratamento de erro), salva isso em "animal"
            animal = linha.strip().split(";")
            # Checa se o primeiro elemento da lista (nome do pet) é igual ao inserido pelo usuário
            if animal[0] == excluir:
                encontrado = True
                continue
            else:
                # Caso o nome não seja igual, reescreve a linha original (impede que seja sobrescrita).
                file.write(linha)
        if not encontrado:
            print("Animal não encontrado.")
        else:
            print("Animal excluido com sucesso.")
   

def registrar_evento():
    # Guarda o evento desejado pelo usuário em opção                        
    print("Qual evento você deseja registrar?")     
    opcao = int(input("1- Vacinações, 2- Consultas Veterinárias, 3- Aplicações de remédios\n"))

    # Caso a opção inserida seja inválida, pergunta novamente até que seja (tratamento de erro)
    if opcao < 1 or opcao > 3:
        while opcao < 1 or opcao > 3:
            opcao = int(input("Opção inválida. Escolha uma das opções citadas: "))

    # Opção vacinações
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
        
    # Opção consultas veterinárias
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

            # Salva o compromisso no arquivo consultas.txt
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
    
    # Opção aplicação de remédios
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

            # Salva o compromisso no arquivo aplicacoes.txt
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

def definir_metas():
    nome = input("Você deseja definir metas para que pet? ")
    pet_encontrado = False

    # Verifica se o pet existe no arquivo 
    with open("file.txt", "r", encoding="utf8") as file:
            for linha in file:
                dados = linha.strip().split(";")
                if dados and dados[0].lower() == nome.lower():
                    pet_encontrado = True
                    break
    
    if pet_encontrado:
        meta = input("Que meta você deseja definir: ")

        # Salva a meta em "metas.txt"
        with open("metas.txt", "a", encoding="utf8") as file:
            file.write(f"Pet: {nome}\n")
            file.write(f"Meta: {meta}\n\n")
        
        print(f"Meta marcada com sucesso para {nome}")

    else:
         print(f"O pet '{nome}' não foi encontrado no registro. Por favor, registre o pet primeiro.")


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
    opcao = int(input("1- Adicionar um pet, 2- Visualizar um pet, 3- Editar um pet ja existente, 4- Excluir um pet, 5- Registrar eventos, 6- Definir metas, 7- Sair\n"))
    
    if opcao == 1:
        adicionar_animal()      

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
        definir_metas()
        
    elif opcao == 7:
        print("Obrigado por usar Vida Pet!")
        break
    else:
        while opcao < 1 or opcao > 5:
            opcao = int(input("Opção inválida. Digite uma opção dentro das disponíveis: "))
        

