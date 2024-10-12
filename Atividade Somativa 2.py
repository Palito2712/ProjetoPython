# - Nome: Luis Felipe Schueda
# - Curso: Superior de Tecnologia em Big Data e Inteligência Analítica

import json


def salvar_arquivo(lista, nome_arquivo):
    # Abrir o arquivo em modo escrever e salvar a lista de dicionários no nosso arquivo que está aberto
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_aberto:
        json.dump(lista, arquivo_aberto, ensure_ascii=False)
        # Feito esse processo, fechamos o arquivo.
        arquivo_aberto.close()


def carregar_arquivo(nome_arquivo):
    # Se ele abrir o arquivo, ele nos retornará a lista de dicionários.
    try:
        with open(nome_arquivo, 'r') as arquivo_aberto:
            lista = json.load(arquivo_aberto)
            return lista
    except FileNotFoundError:
        # Caso contrário, se não abrir, significa que não há o arquivo, logo, retornará uma lista vazia para comerçarmos
        # a trabalhar com as informações.
        return []


def mostrar_menu_principal():
    # Mostrar menu principal ao usuário e coletamos a opção desejada.
    print("Olá, bem vindo ao nosso menu principal!")
    print("     1 - Estudantes")
    print("     2 - Professores")
    print("     3 - Disciplinas")
    print("     4 - Turmas")
    print("     5 - Matrículas")
    print("     0 - Sair")
    return input("Por favor, digite o número da opção desejada: ")


def mostrar_menu_operacoes(opcao_primaria):
    # Mostrar menu de operações de cada opção do menu principal e coletamos a opção desejada.
    print("     1 - Listar")
    print("     2 - Incluir")
    print("     3 - Atualizar")
    print("     4 - Excluir")
    print("     0 - Retornar ao menu principal")
    return input("Por favor, digite o número da opção desejada: ")


def listagem(opcao_secundaria, nome_arquivo):

    print(f"Você escolheu a opção {opcao_secundaria} - LISTAR")

    lista = carregar_arquivo(nome_arquivo)   # Carregando o arquivo desejado para utilização dos cadastros.

    if len(lista) == 0:
        # Se a lista for vazia, não há cadastros.
        print("Não há nenhum cadastrado no momento!")
    else:
        print("Lista de cadastros realizados: ")
        # Se não for vazia, para cada cadastro, mostre cada elemento dessa lista.
        for cada in lista:
            print('-', cada)


def incluir(opcao_secundaria, nome_arquivo):
    if opcao_primaria == '1':
        # Solicitando ao usuário as informações do estudante que deseja incluir
        print(f"Você selecionou a opção: {opcao_secundaria} - INCLUIR")
        while True:
            try:          # Verificar se o usuário digitou apenas números inteiros
                codigo_estudante = int(input("Digite o código a ser cadastrado: "))
                break
            except ValueError:
                print("Código inválido. Apenas números inteiros são válidos para o cadastro!")
        lista = carregar_arquivo(nome_arquivo)  # Abrindo o arquivo dos estudantes

        for estudante in lista:        # Percorre cada dicionário dentro da lista e verifica se o código digitado pelo
            if estudante["Codigo"] == codigo_estudante:                                           # usuário já existe.
                print(f"O código -{codigo_estudante}- já está cadastrado! Retornando ao menu de operações.")
                break                   # Caso exista, encerramos o loop.

        else:                           # Caso não exista, continuaremos com o cadastro.
            nome_estudante = str(input("Digite o nome da pessoa que deseja incluir: "))
            cpf_estudante = str(input("Por favor, digite o CPF: "))

            # Criando o dicionário com as informações do usuário e anexando na lista.
            dicionario = {}
            dicionario["Codigo"] = codigo_estudante
            dicionario["Nome"] = nome_estudante
            dicionario["CPF"] = cpf_estudante

            lista.append(dicionario)                                  # Anexando o dicionário criado na lista

            print(f"-{nome_estudante}- foi adicionado(a) com sucesso!")

            salvar_arquivo(lista, nome_arquivo)                        # Arquivo salvo com a inclusão feita

    elif opcao_primaria == '2':
        # Solicitando ao usuário as informações do professor que deseja incluir
        print(f"Você selecionou a opção: {opcao_secundaria} - INCLUIR")
        while True:
            try:           # Verificar se o usuário digitou apenas números inteiros
                codigo_professor = int(input("Digite o código a ser cadastrado: "))
                break
            except ValueError:
                print("Código inválido. Apenas números inteiros são válidos para o cadastro!")
        lista = carregar_arquivo(nome_arquivo)  # Abrindo o arquivo dos professores.

        for professor in lista:        # Percorre cada dicionário dentro da lista e verifica se o código digitado pelo
            if professor["Codigo"] == codigo_professor:                                           # usuário já existe.
                print(f"O código -{codigo_professor}- já está cadastrado! Retornando ao menu de operações.")
                break                   # Caso exista, encerramos o loop.

        else:                           # Caso não exista, continuaremos com o cadastro.
            nome_professor = str(input("Digite o nome da pessoa que deseja incluir: "))
            cpf_professor = str(input("Por favor, digite o CPF: "))

            # Criando o dicionário com as informações do usuário e anexando na lista.
            dicionario = {}
            dicionario["Codigo"] = codigo_professor
            dicionario["Nome"] = nome_professor
            dicionario["CPF"] = cpf_professor

            lista.append(dicionario)                                  # Anexando este dicionário na lista

            print(f"-{nome_professor}- foi adicionado(a) com sucesso!")

            salvar_arquivo(lista, nome_arquivo)                       # Arquivo salvo com a inclusão feita

    elif opcao_primaria == '3':
        # Solicitando ao usuário as informações da disciplina que deseja incluir
        print(f"Você selecionou a opção: {opcao_secundaria} - INCLUIR")
        while True:
            try:                        # Verificar se o usuário digitou apenas números inteiros
                codigo_disciplina = int(input("Digite o código da disciplina a ser cadastrado: "))
                break
            except ValueError:
                print("Código inválido. Apenas números inteiros são válidos para o cadastro da disciplina!")
        lista = carregar_arquivo(nome_arquivo)  # Abrindo o arquivo das disciplinas

        for disciplina in lista:        # Percorre cada dicionário dentro da lista e verifica se o código digitado pelo
            if disciplina["Codigo"] == codigo_disciplina:                                           # usuário já existe.
                print(f"O código -{codigo_disciplina}- já está cadastrado! Retornando ao menu de operações.")
                break                   # Caso exista, encerramos o loop.

        else:                           # Caso não exista, continuaremos com o cadastro.
            nome_disciplina = str(input("Digite o nome da disciplina que deseja incluir: "))

            # Criando o dicionário com as informações do usuário e anexando na lista.
            dicionario = {}
            dicionario["Codigo"] = codigo_disciplina
            dicionario["Nome"] = nome_disciplina

            lista.append(dicionario)                                  # Anexando este dicionário na lista

            print(f"A disciplina -{nome_disciplina}- foi adicionada com sucesso!")
            salvar_arquivo(lista, nome_arquivo)                       # Arquivo salvo com a inclusão feita

    elif opcao_primaria == '4':
        # Solicitando ao usuário as informações da turma que deseja incluir
        print(f"Você selecionou a opção: {opcao_secundaria} - INCLUIR")
        while True:
            try:               # Verificar se o usuário digitou apenas números inteiros
                codigo_turma = int(input("Digite o código da turma a ser cadastrado: "))
                break
            except ValueError:
                print("Código inválido. Apenas números inteiros são válidos para o código da turma!")
        lista = carregar_arquivo(nome_arquivo)  # Abrindo o arquivo das turmas

        for turma in lista:             # Percorre cada dicionário dentro da lista e verifica se o código digitado pelo
            if turma["Codigo_Turma"] == codigo_turma:                                               # usuário já existe.
                print(f"O código -{codigo_turma}- já está cadastrado! Retornando ao menu de operações.")
                break                   # Caso exista, encerramos o loop.

        else:                           # Caso não exista, continuaremos com a inclusão dos dados.
            while True:
                try:            # Verificar se o usuário digitou apenas números inteiros
                    codigo_professor = int(input("Digite o código do professor(a): "))
                    break
                except ValueError:
                    print("Código inválido. Apenas números inteiros são válidos para o código do professor!")
            while True:
                try:            # Verificar se o usuário digitou apenas números inteiros
                    codigo_disciplina_turma = int(input("Por favor, digite o código da disciplina: "))
                    break
                except ValueError:
                    print("Código inválido. Apenas números inteiros são válidos para o código da disciplina!")

            # Criando o dicionário com as informações do usuário e anexando na lista.
            dicionario = {}
            dicionario["Codigo_Turma"] = codigo_turma
            dicionario["Codigo_Professor"] = codigo_professor
            dicionario["Codigo_Disciplina_Turma"] = codigo_disciplina_turma

            lista.append(dicionario)                                  # Anexando este dicionário na lista

            print(f"A turma -{codigo_turma}- foi adicionada com sucesso!")
            salvar_arquivo(lista, nome_arquivo)                       # Arquivo salvo com a inclusão feita

    elif opcao_primaria == '5':
        # Solicitando ao usuário as informações da matrícula que deseja incluir
        print(f"Você selecionou a opção: {opcao_secundaria} - INCLUIR")
        while True:
            try:                    # Verificar se o usuário digitou apenas números inteiros
                codigo_matricula = int(input("Digite o código da matrícula a ser cadastrada: "))
                break
            except ValueError:
                print("Código inválido. Apenas números inteiros são válidos para o código da matrícula!")
        lista = carregar_arquivo(nome_arquivo)  # Abrindo o arquivo das matrículas.

        for matricula in lista:          # Percorre cada dicionário dentro da lista e verifica se o código digitado pelo
            if matricula["Codigo_Matricula"] == codigo_matricula:                                   # usuário já existe.
                print(f"O código -{codigo_matricula}- já está cadastrado! Retornando ao menu de operações.")
                break                    # Caso exista, encerramos o loop.

        else:                            # Caso não exista, continuaremos com a inclusão dos dados.
            while True:
                try:                    # Verificar se o usuário digitou apenas números inteiros
                    codigo_estudante = int(input("Digite o código do estudante que deseja incluir: "))
                    break
                except ValueError:
                    print("Código inválido. Apenas números inteiros são válidos para o código do estudante!")
            # Criando o dicionário com as informações do usuário e anexando na lista.
            dicionario = {}
            dicionario["Codigo_Matricula"] = codigo_matricula
            dicionario["Codigo_Estudante"] = codigo_estudante

            lista.append(dicionario)                                  # Anexando este dicionário na lista

            print(f"A matrícula -{codigo_matricula}- foi adicionada com sucesso!")
            salvar_arquivo(lista, nome_arquivo)                       # Arquivo salvo com a inclusão feita


def atualizar(opcao_secundaria, nome_arquivo):
    if opcao_primaria == '1' or opcao_primaria == '2':
        # Se a opção for estudante OU professor:
        print(f"Você escolheu a opção: {opcao_secundaria} - ATUALIZAR")

        atualizar = None                                    # Variável temporária
        while True:
            try:                                            # Verificar se o usuário digitou apenas números inteiros
                codigo_editar = int(input("Por favor, digite o código do cadastro que deseja atualizar: "))
                break
            except ValueError:
                print("Código inválido. Apenas números inteiros são válidos para o cadastro!")

        lista = carregar_arquivo(nome_arquivo)              # Carregando o arquivo desejado
        for dicionario in lista:                            # Percorre cada dicionário dentro da lista.
            if dicionario["Codigo"] == codigo_editar:       # Se o código digitado pelo usuário for encontrado
                atualizar = dicionario                      # no dicionário, ele entrará na variável temporária
                break                                       # para que possamos atualizar as informações.

        if atualizar is None:
            print(f"O código: {codigo_editar} não foi encontrado na seguinte lista: ")
            # Se a variável temporária ainda for none, quer dizer que o código não foi encontrado no dicionário.

        else:   # Coletando do usuário os novos valores a serem atualizados após o código ser encontrado.
            while True:
                try:                                        # Verificar se o usuário digitou apenas números inteiros
                    atualizar["Codigo"] = int(input("Digite o novo código para o cadastro: "))
                    break
                except ValueError:
                    print("Código inválido. Digite apenas números inteiros para o cadastro!")

            atualizar["Nome"] = str(input("Por favor, digite o nome: "))
            atualizar["CPF"] = str(input("Agora digite o CPF: "))

            for atualizacao in lista:
                print(atualizacao)                              # Mostrando as informações que foram atualizadas.

            print("Cadastro atualizado com sucesso! Retornando ao menu de operações. ")

            salvar_arquivo(lista, nome_arquivo)                 # Arquivo salvo com as alterações feitas
    elif opcao_primaria == '3':

        print(f"Você escolheu a opção: {opcao_secundaria} - ATUALIZAR")

        atualizar_disciplina = None                             # Variável temporária
        while True:
            try:                                                # Verificar se o usuário digitou apenas números inteiros
                codigo_disciplina_editar = int(input("Por favor, digite o código do cadastro que deseja atualizar: "))
                break
            except ValueError:
                print("Código inválido. Apenas números inteiros são válidos para o cadastro!")
        lista = carregar_arquivo(nome_arquivo)                  # Carregando o arquivo das disciplinas

        for dicionario_disciplina in lista:                     # Percorre cada dicionário dentro da lista.
            if dicionario_disciplina["Codigo"] == codigo_disciplina_editar:
                atualizar_disciplina = dicionario_disciplina    # Se o código digitado pelo usuário for encontrado
                break                                           # no dicionário, ele entrará na variável temporária
                                                                # para que possamos atualizar as informações.
        if atualizar_disciplina is None:
            print(f"O código: {codigo_disciplina_editar} não foi encontrado na seguinte lista: ")
            # Se a variável temporária ainda for none, quer dizer que o código não foi encontrado no dicionário.

        else:  # Coletando do usuário os novos valores a serem atualizados após o código ser encontrado
            while True:
                try:                                            # Verificar se o usuário digitou apenas números inteiros
                    atualizar_disciplina["Codigo"] = int(input("Digite o novo código para a disciplina: "))
                    break
                except ValueError:
                    print("Código inválido. Apenas números inteiros são válidos para o código da disciplina!")

            atualizar_disciplina["Nome"] = str(input("Por favor, digite o nome da disciplina: "))

            for atualizacao in lista:
                print(atualizacao)                                  # Mostrando as informações que foram atualizadas.

            print("Cadastro atualizado com sucesso! Retornando ao menu de operações. ")
            salvar_arquivo(lista, nome_arquivo)                     # Arquivo salvo com as alterações feitas

    elif opcao_primaria == '4':
        print(f"Você escolheu a opção: {opcao_secundaria} - ATUALIZAR")

        atualizar_turma = None                                  # Variável temporária
        while True:
            try:                                                # Verificar se o usuário digitou apenas números inteiros
                codigo_editar_turma = int(input("Por favor, digite o código do cadastro que deseja atualizar: "))
                break
            except ValueError:
                print("Código inválido. Apenas números inteiros são válidos para o cadastro!")
        lista = carregar_arquivo(nome_arquivo)                  # Carregando o arquivo da turma

        for dicionario_turma in lista:                          # Percorre cada dicionário dentro da lista.
            if dicionario_turma["Codigo_Turma"] == codigo_editar_turma:
                atualizar_turma = dicionario_turma              # Se o código digitado pelo usuário for encontrado
                break                                           # no dicionário, ele entrará na variável temporária
                                                                # para que possamos atualizar as informações.
        if atualizar_turma is None:
            print(f"O código: {codigo_editar_turma} não foi encontrado na seguinte lista: ")
            # Se a variável temporária ainda for none, quer dizer que o código não foi encontrado no dicionário.

        else:  # Coletando do usuário os novos valores a serem atualizados após o código ser encontrado
            while True:
                try:                                            # Verificar se o usuário digitou apenas números inteiros
                    atualizar_turma["Codigo_Turma"] = int(input("Digite o novo código para o cadastro da turma: "))
                    break
                except ValueError:
                    print("Código inválido. Apenas números inteiros são válidos para o código da turma!")
            while True:
                try:                                            # Verificar se o usuário digitou apenas números inteiros
                    atualizar_turma["Codigo_Professor"] = int(input("Por favor, digite o código do professor: "))
                    break
                except ValueError:
                    print("Código inválido. Apenas números inteiros são válidos para o código do professor!")
            while True:
                try:                                            # Verificar se o usuário digitou apenas números inteiros
                    atualizar_turma["Codigo_Disciplina_Turma"] = int(input("Agora digite o código da disciplina: "))
                    break
                except ValueError:
                    print("Código inválido. Apenas números inteiros são válidos para o código da disciplina!")

            for atualizacao in lista:
                print(atualizacao)                              # Mostrando as informações que foram atualizadas.

            print("Cadastro atualizado com sucesso! Retornando ao menu de operações. ")
            salvar_arquivo(lista, nome_arquivo)                 # Arquivo salvo com as alterações feitas

    elif opcao_primaria == '5':

        print(f"Você escolheu a opção: {opcao_secundaria} - ATUALIZAR")

        atualizar_matricula = None                              # Variável temporária

        while True:
            try:                                                # Verificar se o usuário digitou apenas números inteiros
                codigo_matricula_editar = int(input("Por favor, digite o código do cadastro que deseja atualizar: "))
                break
            except ValueError:
                print("Código inválido. Apenas números inteiros são válidos para o cadastro!")

        lista = carregar_arquivo(nome_arquivo)                  # Carrega o arquivo das matrículas

        for dicionario_matricula in lista:                      # Percorre cada dicionário dentro da lista.
            if dicionario_matricula["Codigo_Matricula"] == codigo_matricula_editar:
                atualizar_matricula = dicionario_matricula      # Se o código digitado pelo usuário for encontrado
                break                                           # no dicionário, ele entrará na variável temporária
                                                                # para que possamos atualizar as informações.
        if atualizar_matricula is None:
            print(f"O código: {codigo_matricula_editar} não foi encontrado na seguinte lista: ")
            # Se a variável temporária ainda for none, quer dizer que o código não foi encontrado no dicionário.

        else:  # Coletando do usuário os novos valores a serem atualizados após o código ser encontrado
            while True:
                try:                                            # Verificar se o usuário digitou apenas números inteiros
                    atualizar_matricula["Codigo_Matricula"] = int(input("Digite o novo código para a matrícula: "))
                    break
                except ValueError:
                    print("Código inválido. Apenas números inteiros são válidos para o cadastro da matrícula!")
            while True:
                try:                                            # Verificar se o usuário digitou apenas números inteiros
                    atualizar_matricula["Codigo_Estudante"] = int(input("Por favor, digite o código do estudante: "))
                    break
                except ValueError:
                    print("Código inválido. Apenas números inteiros são válidos para o código do estudante!")

            for atualizacao in lista:
                print(atualizacao)                              # Mostrando as informações que foram atualizadas.

            print("Cadastro atualizado com sucesso! Retornando ao menu de operações. ")
            salvar_arquivo(lista, nome_arquivo)                 # Arquivo salvo com as alterações feitas


def deletar(opcao_secundaria, nome_arquivo):

    if opcao_primaria == '1' or opcao_primaria == '2' or opcao_primaria == '3':
        # Se a opção for estudante, professor ou disciplinas, executaremos os seguintes códigos, assim, reaproveitamos.
        print(f"Você escolheu a opção: {opcao_secundaria} - EXCLUIR")

        deletar = None                                          # Variável temporária
        lista = carregar_arquivo(nome_arquivo)                  # Carrega o arquivo desejado

        while True:
            try:                                                # Verificar se o usuário digitou apenas números inteiros
                codigo_excluir = int(input("Por favor, digite o código do cadastro que deseja excluir: "))
                break
            except ValueError:
                print("Código inválido. Apenas números inteiros são válidos para o cadastro!")

        for dicionario in lista:                                # Percorre cada dicionário dentro da lista
            if dicionario["Codigo"] == codigo_excluir:
                deletar = dicionario                            # Se o código digitado pelo usuário for encontrado
                break                                           # no dicionário, ele entrará na variável temporária
                                                                # para que depois possamos deletar.
        if deletar is None:
            print(f"O código: {codigo_excluir} não foi encontrado na lista!")
            # Se a variável temporária ainda for none, quer dizer que o código não foi encontrado no dicionário.
        else:

            lista.remove(deletar)                   # Com o código encontrado, ele é removido e então o arquivo é salvo
            salvar_arquivo(lista, nome_arquivo)                                                # com a devida alteração
            print("Cadastro removido com sucesso!")

    elif opcao_primaria == '4':
        # Se a opção for turmas:
        print(f"Você escolheu a opção: {opcao_secundaria} - EXCLUIR")

        deletar_turma = None                                # Variável temporária
        lista = carregar_arquivo(nome_arquivo)              # Carrega o arquivo da turma
        while True:
            try:                                            # Verificar se o usuário digitou apenas números inteiros
                codigo_excluir_turma = int(input("Por favor, digite o código da turma que deseja excluir: "))
                break
            except ValueError:
                print("Código inválido. Apenas números inteiros são válidos para o código da turma!")

        for dicionario in lista:                            # Percorre cada dicionário dentro da lista
            if dicionario["Codigo_Turma"] == codigo_excluir_turma:
                deletar_turma = dicionario                  # Se o código digitado pelo usuário for encontrado
                break                                       # no dicionário, ele entrará na variável temporária
                                                            # para que depois possamos deletar.
        if deletar_turma is None:
            print(f"O código: {codigo_excluir_turma} não foi encontrado na lista!")
            # Se a variável temporária ainda for none, quer dizer que o código não foi encontrado no dicionário.
        else:
            lista.remove(deletar_turma)     # Com o código encontrado, ele é removido e então o arquivo é salvo
            salvar_arquivo(lista, nome_arquivo)                                        # com a devida alteração
            print("Cadastro removido com sucesso!")

    elif opcao_primaria == '5':
        # Se a opção for matrículas:
        print(f"Você escolheu a opção: {opcao_secundaria} - EXCLUIR")

        deletar_matricula = None                                # Variável temporária
        lista = carregar_arquivo(nome_arquivo)                  # Carrega o arquivo de matrícula

        while True:
            try:                                                # Verificar se o usuário digitou apenas números inteiros
                codigo_excluir_matricula = int(input("Por favor, digite o código da matrícula que deseja excluir: "))
                break
            except ValueError:
                print("Código inválido. Apenas números inteiros são válidos para o código da matrícula!")

        for dicionario in lista:                                # Percorre cada dicionário dentro da lista
            if dicionario["Codigo_Matricula"] == codigo_excluir_matricula:
                deletar_matricula = dicionario                  # Se o código digitado pelo usuário for encontrado
                break                                           # no dicionário, ele entrará na variável temporária
                                                                # para que depois possamos deletar
        if deletar_matricula is None:
            print(f"A matrícula: {codigo_excluir_matricula} não foi encontrada na lista!")
            # Se a variável temporária ainda for none, quer dizer que o código não foi encontrado no dicionário.
        else:
            lista.remove(deletar_matricula)         # Com o código encontrado, ele é removido e então o arquivo é salvo
            salvar_arquivo(lista, nome_arquivo)                                                # com a devida alteração
            print("Matrícula removida com sucesso!")


arquivo_estudante = "Estudantes.json"           # Arquivos criados para persistência dos dados.
arquivo_professor = "Professores.json"
arquivo_disciplina = "Disciplinas.json"
arquivo_turma = "Turmas.json"
arquivo_matricula = "Matriculas.json"

while True:
    # Mostrando o nosso menu principal ao usuário e coletando a sua opção desejada.
    opcao_primaria = mostrar_menu_principal()

    if opcao_primaria == '1':
        # Se a opção for estudantes:
        print(f"Você escolheu a opção: {opcao_primaria}")
        while True:

            print(f"Aqui está o menu de operações da opção: {opcao_primaria} - ESTUDANTES")
            opcao_secundaria = mostrar_menu_operacoes(opcao_primaria)
            # Mostrando o menu de operações.
            # Coletando a opção do usuário no menu de operações.

            if opcao_secundaria == '1':
                # Se a opção no menu de operações for listar, chama a função listagem com a opção digitada e o arquivo
                listagem(opcao_secundaria, arquivo_estudante)                                        # como parâmetros

            elif opcao_secundaria == '2':
                # Se a opção no menu de operações for incluir, chama a função incluir com a opção digitada e o arquivo
                incluir(opcao_secundaria, arquivo_estudante)                                         # como parâmetros

            elif opcao_secundaria == '3':
                # Se a opção no menu de operações for atualizar, chama a função atualizar com a opção digitada e o
                atualizar(opcao_secundaria, arquivo_estudante)                           # arquivo como parâmetros

            elif opcao_secundaria == '4':
                # Se a opção no menu de operações for excluir, chama a função deletar com a opção digitada e o arquivo
                deletar(opcao_secundaria, arquivo_estudante)                                         # como parâmetros

            elif opcao_secundaria == '0':
                # Se o usuário digitar 0, sair do menu de operações e retornar ao menu principal.
                print(f"Você selecionou a opção: {opcao_secundaria} - RETORNAR AO MENU PRINCIPAL")
                break  # Interrompendo o loop secundário e retornando ao loop primário, menu principal.

            else:
                # Caso a opção digitada seja qualquer outra, irá mostrar novamente o menu de operações
                print(f"A opção {opcao_secundaria} é inválida! Por favor, digite uma opção válida!!")

    elif opcao_primaria == '2':
        # Se a opção for professores:
        print(f"Você escolheu a opção {opcao_primaria}")

        while True:

            print(f"Aqui está o menu de operações da opção: {opcao_primaria} - PROFESSORES")
            opcao_secundaria = mostrar_menu_operacoes(opcao_primaria)
            # Mostrando o menu de operações.
            # Coletando a opção do usuário no menu de operações.

            if opcao_secundaria == '1':
                # Se a opção no menu de operações for listar, chama a função listagem com a opção digitada e o arquivo
                listagem(opcao_secundaria, arquivo_professor)                                        # como parâmetros

            elif opcao_secundaria == '2':
                # Se a opção no menu de operações for incluir, chama a função incluir com a opção digitada e o arquivo
                incluir(opcao_secundaria, arquivo_professor)                                         # como parâmetros

            elif opcao_secundaria == '3':
                # Se a opção no menu de operações for atualizar, chama a função atualizar com a opção digitada e o
                atualizar(opcao_secundaria, arquivo_professor)                           # arquivo como parâmetros

            elif opcao_secundaria == '4':
                # Se a opção no menu de operações for excluir, chama a função deletar com a opção digitada e o arquivo
                deletar(opcao_secundaria, arquivo_professor)                                         # como parâmetros

            elif opcao_secundaria == '0':
                # Se o usuário digitar 0, sair do menu de operações e retornar ao menu principal.
                print(f"Você selecionou a opção: {opcao_secundaria} - RETORNAR AO MENU PRINCIPAL")
                break  # Interrompendo o loop secundário e retornando ao loop primário, menu principal.

            else:
                # Caso a opção digitada seja qualquer outra, irá mostrar novamente o menu de operações
                print(f"A opção {opcao_secundaria} é inválida! Por favor, digite uma opção válida!!")

    elif opcao_primaria == '3':
        # Se a opção for disciplinas:
        print(f"Você escolheu a opção {opcao_primaria}")
        while True:

            print(f"Aqui está o menu de operações da opção: {opcao_primaria} - DISCIPLINAS")
            opcao_secundaria = mostrar_menu_operacoes(opcao_primaria)
            # Mostrando o menu de operações.
            # Coletando a opção do usuário no menu de operações.

            if opcao_secundaria == '1':
                # Se a opção no menu de operações for excluir, chama a função listagem com a opção digitada e o arquivo
                listagem(opcao_secundaria, arquivo_disciplina)                                        # como parâmetros

            elif opcao_secundaria == '2':
                # Se a opção no menu de operações for incluir, chama a função incluir com a opção digitada e o arquivo
                incluir(opcao_secundaria, arquivo_disciplina)                                         # como parâmetros

            elif opcao_secundaria == '3':
                # Se a opção no menu de operações for atualizar, chama a função atualizar com a opção digitada e o
                atualizar(opcao_secundaria, arquivo_disciplina)                         # arquivo como parâmetros

            elif opcao_secundaria == '4':
                # Se a opção no menu de operações for excluir, chama a função deletar com a opção digitada e o arquivo
                deletar(opcao_secundaria, arquivo_disciplina)                                         # como parâmetros

            elif opcao_secundaria == '0':
                # Se o usuário digitar 0, sair do menu de operações e retornar ao menu principal.
                print(f"Você selecionou a opção: {opcao_secundaria} - RETORNAR AO MENU PRINCIPAL")
                break  # Interrompendo o loop secundário e retornando ao loop primário, menu principal.

            else:
                # Caso a opção digitada seja qualquer outra, irá mostrar novamente o menu de operações
                print(f"A opção {opcao_secundaria} é inválida! Por favor, digite uma opção válida!!")

    elif opcao_primaria == '4':
        # Se a opção for turmas:
        print(f"Você escolheu a opção {opcao_primaria}")

        while True:

            print(f"Aqui está o menu de operações da opção: {opcao_primaria} - TURMAS")
            opcao_secundaria = mostrar_menu_operacoes(opcao_primaria)
            # Mostrando o menu de operações.
            # Coletando a opção do usuário no menu de operações.

            if opcao_secundaria == '1':
                # Se a opção no menu de operações for listar, chama a função listagem com a opção digitada e o arquivo
                listagem(opcao_secundaria, arquivo_turma)                                            # como parâmetros

            elif opcao_secundaria == '2':
                # Se a opção no menu de operações for incluir, chama a função incluir com a opção digitada e o arquivo
                incluir(opcao_secundaria, arquivo_turma)                                              # como parâmetros

            elif opcao_secundaria == '3':
                # Se a opção no menu de operações for atualizar, chama a função atualizar com a opção digitada e o
                atualizar(opcao_secundaria, arquivo_turma)                              # arquivo como parâmetros

            elif opcao_secundaria == '4':
                # Se a opção no menu de operações for excluir, chama a função deletar com a opção digitada e o arquivo
                deletar(opcao_secundaria, arquivo_turma)                                              # como parâmetros

            elif opcao_secundaria == '0':
                # Se o usuário digitar 0, sair do menu de operações e retornar ao menu principal.
                print(f"Você selecionou a opção: {opcao_secundaria} - RETORNAR AO MENU PRINCIPAL")
                break  # Interrompendo o loop secundário e retornando ao loop primário, menu principal.

            else:
                # Caso a opção digitada seja qualquer outra, irá mostrar novamente o menu de operações
                print(f"A opção {opcao_secundaria} é inválida! Por favor, digite uma opção válida!!")

    elif opcao_primaria == '5':
        # Se a opção for matrículas:
        print(f"Você escolheu a opção {opcao_primaria}")

        while True:

            print(f"Aqui está o menu de operações da opção: {opcao_primaria} - MATRÍCULAS")
            opcao_secundaria = mostrar_menu_operacoes(opcao_primaria)
            # Mostrando o menu de operações.
            # Coletando a opção do usuário no menu de operações.

            if opcao_secundaria == '1':
                # Se a opção no menu de operações for listar, chama a função listagem com a opção digitada e o arquivo
                listagem(opcao_secundaria, arquivo_matricula)                                        # como parâmetros

            elif opcao_secundaria == '2':
                # Se a opção no menu de operações for incluir, chama a função incluir com a opção digitada e o arquivo
                incluir(opcao_secundaria, arquivo_matricula)                                         # como parâmetros

            elif opcao_secundaria == '3':
                # Se a opção no menu de operações for atualizar, chama a função atualizar com a opção digitada e o
                atualizar(opcao_secundaria, arquivo_matricula)                           # arquivo como parâmetros

            elif opcao_secundaria == '4':
                # Se a opção no menu de operações for excluir, chama a função deletar com a opção digitada e o arquivo
                deletar(opcao_secundaria, arquivo_matricula)                                         # como parâmetros

            elif opcao_secundaria == '0':
                # Se o usuário digitar 0, sair do menu de operações e retornar ao menu principal.
                print(f"Você selecionou a opção: {opcao_secundaria} - RETORNAR AO MENU PRINCIPAL")
                break  # Interrompendo o loop secundário e retornando ao loop primário, menu principal.

            else:
                # Caso a opção digitada seja qualquer outra, irá mostrar novamente o menu de operações
                print(f"A opção {opcao_secundaria} é inválida! Por favor, digite uma opção válida!!")

    elif opcao_primaria == '0':
        # Se a opção for sair:
        print("Você saiu do menu. Até a próxima!")
        break  # Interrompendo o loop primário e encerrando a execução

    else:
        print(f"A opção {opcao_primaria} é inválida! Por favor, digite uma opção válida!!")
        # Caso a opção digitada seja qualquer outra, irá mostrar novamente o menu principal
