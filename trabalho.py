import os
os.system("cls")

def adicionar_animal():
    nome = input("Digite o nome do animal: ")
    especie = input(f"Digite a especie de {nome}: ")
    raca = input(f"Digite a raça de {nome}: ")
    datanasc = input(f"Digite a data de nascimento de {nome}: ")
    peso = input (f"Digite o peso de {nome}: ")
    informacoes = f"{nome};{especie};{raca};{datanasc};{peso}"
    with open("file.txt", "a", encoding='utf8') as file:
        file.writelines(informacoes + "\n")
    print("Pet adicionado.")


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


def editar_animal():    
    editar = input("Digite o nome do animal que você quer editar: ")
    encontrado = False

    with open("file.txt", "r", encoding="utf8") as file:
        linhas = file.readlines()

    with open("file.txt", "r+", encoding="utf8") as file:
        for linha in linhas:
            animais = linha.strip().split(";")
            if len(animais) < 5:
                file.write(linha)
                continue
            
            if animais[0].lower() == editar.lower():
                nome = input("Escreva o nome do novo animal: ")
                especie = input(f"Digite a espécie de {nome}: ")
                raca = input(f"Digite a raça de {nome}: ")
                datanascimento = input(f"Digite a data de nascimento de {nome} (dd/mm/aaaa): ")
                peso = input(f"Digite o peso de {nome}: ")
                nova_linha = f"{nome};{especie};{raca};{datanascimento};{peso}\n"
                file.write(nova_linha)
                encontrado = True
            else:
                file.write(linha)

    if encontrado:
        print("Animal editado com sucesso.")
    else:
        print("Animal não encontrado.")
    

def excluir_animal():  
    excluir = input("Digite o nome do animal que você quer excluir: ").lower()
    encontrado = False

    with open("file.txt", 'r', encoding="utf-8") as file:
        linhas = file.readlines()

    with open("file.txt", 'w', encoding="utf-8") as file:
        for linha in linhas:
            animal = linha.strip().split(";")
            if animal[0].lower() == excluir:
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
    opcao = input("1- Vacinações, 2- Consultas Veterinárias, 3- Aplicações de remédios\n")

    if opcao != "1" and opcao != "2" and opcao != "3" and opcao.isdigit() == False:
        while opcao != "1" and opcao != "2" and opcao != "3" and opcao.isdigit() == False:
            opcao = input("Opção inválida. Escolha uma das opções citadas: ")

    if opcao == 1:
        nome = input("Você quer marcar a vacinação para que pet? ")

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

            with open("vacinas.txt", "a", encoding="utf8") as file:
                file.write(f"Pet: {nome}\n")
                file.write(f"Data da vacinação: {data_vacinacao}\n")
                file.write(f"Observações: {observacao}\n\n")

            print(f"Vacinação marcada com sucesso para o pet {nome}.")
        else:
            print(f"O pet '{nome}' não foi encontrado no registro. Por favor, registre o pet primeiro.")
    
        
    elif opcao == 2:
        nome = input("Você quer marcar a consulta para que pet? ")

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

            with open("consultas.txt", "a", encoding="utf8") as file:
                file.write(f"Pet: {nome}\n")
                file.write(f"Data da consulta: {data_consulta}\n")
                file.write(f"Observações: {observacao}\n\n")

            print(f"Consulta marcada com sucesso para o pet {nome}.")
        else:
            print(f"O pet '{nome}' não foi encontrado no registro. Por favor, registre o pet primeiro.")
    
    else:
        nome = input("Você quer marcar a aplicação para que pet? ")

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

            with open("aplicacoes.txt", "a", encoding="utf8") as file:
                file.write(f"Pet: {nome}\n")
                file.write(f"Data da aplicacao: {data_aplicacao}\n")
                file.write(f"Observações: {observacao}\n\n")

            print(f"Aplicação marcada com sucesso para o pet {nome}.")

        else:
            print(f"O pet '{nome}' não foi encontrado no registro. Por favor, registre o pet primeiro.")

def definir_metas():
    print("O que você deseja fazer:")

    try:
        opcao = int(input("1- Definir uma meta, 2- Acompanhar uma meta: "))
    except ValueError:
        print("Entrada inválida: Insira um dos valores relacionados as opções.")
        return

    if opcao == 1:
        nome = input("Você deseja definir metas para que pet? ").strip()
        pet_encontrado = False

        with open("file.txt", "r", encoding="utf8") as file:
            for linha in file:
                dados = linha.strip().split(";")
                if dados and dados[0].lower() == nome.lower():
                    pet_encontrado = True
                    break
        
        if pet_encontrado:
            nova_meta = input("Que meta você deseja definir: ").strip()

            atualizado = False
            linhas_novas = []
            with open("metas.txt", "r", encoding="utf8") as file:
                linhas = file.readlines()

            i = 0
            while i < len(linhas):
                linha = linhas[i]
                if linha.strip().lower() == f"pet: {nome.lower()}":
                    linhas_novas.append(f"Pet: {nome}\n")
                    linhas_novas.append(f"Meta: {nova_meta}\n")
                    if i + 2 < len(linhas) and linhas[i + 2].strip().lower().startswith("status:"):
                        i += 3
                    else:
                        i += 2
                    atualizado = True
                    continue
                else:
                    linhas_novas.append(linha)
                i += 1

            if not atualizado:
                linhas_novas.append(f"Pet: {nome}\n")
                linhas_novas.append(f"Meta: {nova_meta}\n\n")

            with open("metas.txt", "w", encoding="utf8") as file:
                file.writelines(linhas_novas)

            print(f"Meta atualizada com sucesso para {nome}!")

        else:
            print(f"O pet '{nome}' não foi encontrado no registro. Por favor, registre o pet primeiro.")

    elif opcao == 2:
        nome = input("Você deseja acompanhar as metas para que pet? ").strip()
        pet_encontrado = False

        with open("file.txt", "r", encoding="utf8") as file:
            for linha in file:
                dados = linha.strip().split(";")
                if dados and dados[0].lower() == nome.lower():
                    pet_encontrado = True
                    break
        
        if pet_encontrado:
            with open("metas.txt", "r", encoding="utf8") as file:
                linhas = file.readlines()

            encontrou_meta = False
            linhas_novas = []
            i = 0
            while i < len(linhas):
                linha = linhas[i]
                if linha.strip().lower() == f"pet: {nome.lower()}":
                    encontrou_meta = True
                    print(linha.strip())
                    print(linhas[i + 1].strip())
                    
                    resposta = input("Sua meta está sendo cumprida? (sim/não): ").strip().lower()

                    linhas_novas.append(f"Pet: {nome}\n")
                    linhas_novas.append(linhas[i + 1])

                    if resposta == "sim" or resposta == "não" or resposta == "nao":
                        linhas_novas.append(f"Status: {resposta}\n")
                        print("Status atualizado com sucesso.")
                    else:
                        print("Resposta inválida. Status não foi alterado.")
                    
                    i += 2
                    if i < len(linhas) and linhas[i].strip().lower().startswith("status:"):
                        i += 1
                    continue
                else:
                    linhas_novas.append(linha)
                i += 1

            if encontrou_meta:
                with open("metas.txt", "w", encoding="utf8") as file:
                    file.writelines(linhas_novas)
            else:
                print(f"Não há metas registradas para o pet '{nome}'.")
        else:
            print(f"O pet '{nome}' não foi encontrado no registro. Por favor, registre o pet primeiro.")

    else:
        print("Entrada inválida: Escolha 1 (Definir uma meta) ou 2 (Acompanhar uma meta).")


def sugestoes_cuidados(especie, idade):
    cuidados = {}

    try:
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")
        
        especie = especie.lower()

        if especie == "cachorro":
            if idade < 1:
                cuidados = {
                    "brinquedos": "Brinquedos de borracha macia e mordedores próprios para filhotes",
                    "alimentação": "Ração para filhotes de cachorro (rica em proteínas e cálcio)",
                    "exercício": "Caminhadas curtas e brincadeiras leves\n"
                }
            elif idade < 7:
                cuidados = {
                    "brinquedos": "Bolas resistentes, cordas e brinquedos interativos",
                    "alimentação": "Ração para adultos de acordo com o porte",
                    "exercício": "Caminhadas diárias e atividades físicas moderadas\n"
                }
            else:
                cuidados = {
                    "brinquedos": "Brinquedos de baixo impacto, como pelúcias e mordedores leves",
                    "alimentação": "Ração sênior com menos gordura e suplementos articulares",
                    "exercício": "Exercícios leves e regulares para manter a mobilidade\n"
                }

        elif especie == "gato":
            if idade < 1:
                cuidados = {
                    "brinquedos": "Bolinha com guizo, varinhas com penas e brinquedos pequenos",
                    "alimentação": "Ração para filhotes de gato (com alta energia e taurina)",
                    "exercício": "Brincadeiras curtas com estímulos visuais\n"
                }
            elif idade < 10:
                cuidados = {
                    "brinquedos": "Arranhadores, túneis e brinquedos interativos",
                    "alimentação": "Ração para adultos ou alimentação úmida equilibrada",
                    "exercício": "Brincadeiras diárias para manter o peso ideal\n"
                }
            else:
                cuidados = {
                    "brinquedos": "Brinquedos suaves e arranhadores baixos",
                    "alimentação": "Ração sênior com baixo teor calórico",
                    "exercício": "Estímulos leves e cuidados com articulações\n"
                }

        else:
            cuidados = {
                "mensagem": "Espécie não reconhecida. Por favor, informe 'cachorro' ou 'gato'.\n"
            }

    except ValueError as ve:
        cuidados = {
            "erro": str(ve)
        }

    return cuidados


pets = {}
eventos = {'vacinas': [], 'consultas': [], 'remedios': []}
nome = ''
opcao = 0

while True:
    print("O que você deseja fazer?")
    
    try:
        opcao = int(input("1- Adicionar um pet, \n2- Visualizar um pet, \n3- Editar um pet ja existente, \n4- Excluir um pet," 
                          "\n5- Registrar eventos, \n6- Definir/Atualizar metas, \n7- Visualizar pets para adoção, \n8- Sugestões personalizadas, \n9- Sair\n"))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número entre 1 e 9.")
        continue

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
        import webbrowser
        import os

        caminho_html = os.path.abspath("index.html")
        webbrowser.open(f"file://{caminho_html}")

    elif opcao == 8:
        pet_especie = input("Digite a espécie do pet (cachorro/gato): ")
        pet_idade_input = input("Digite a idade do pet em anos: ")

        try:
            
            pet_idade = float(pet_idade_input)
            sugestao = sugestoes_cuidados(pet_especie, pet_idade)
            print("\nSugestões de cuidados:")
            for chave, valor in sugestao.items():
                print(f"{chave.capitalize()}: {valor}")

        except ValueError:
            print("Idade inválida. Por favor, insira um número válido (ex: 2 ou 5).")
        

    elif opcao == 9:
        print("Obrigado por usar Vida Pet!")
        break

    else:
        print("Opção inválida. Digite um número de 1 e 9.")
        
