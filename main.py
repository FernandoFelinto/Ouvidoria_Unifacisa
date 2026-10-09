'''
PROJETO OUVIDORIA - UNIFACISA
Curso: Análise e Desenvolvimento de Sistemas
Disciplina: Programar em Linguagem Estruturada
Professor: Daniel Abella
Alunos:
- Luiz Fernando Bezerra Felinto (Matrícula: 2625050023)
- Rafael Santos Silva (Matrícula: 2625050010)
- Ricardo Cezar Bispo da Silva (Matrícula: 2625050008)
'''
from metodos import *
from operacoesbd import *

# Cria a conexão com o Banco de Dados "ouvidoria-testes"!
conexao = criarConexao('localhost', 'root','@BDParticular1992','ouvidoria_unifacisa')


while True:
    # MENU PRINCIPAL DA OUVIDORIA
    menu()

    try:
        opcao_usuario = int(input("Digite uma das opções: "))
    except:
        print("Opção inválida!\n")
        continue

    # 1. LISTAR AS MANIFESTAÇÕES
    if opcao_usuario == 1:
        listar_manifestacoes(conexao)

    # 2. REGISTRAR AS MANIFESTAÇÕES
    elif opcao_usuario == 2:
        lista = ['1','2','3','4','5']
        tipo = input("Qual o tipo da sua manifestação?\n1) Reclamação\n2) Sugestão\n3) Elogio\n4) Denúncia\n5) Solicitação\nDigite aqui o número correspondente: ")
        if tipo in lista:
            tipo_escolhido = tipo_manifestacao(tipo)
            manifestacao = input("Digite a sua manifestação: ")
            anonimato = input("Deseja se identificar? (S/N) ").upper()
            if anonimato == 'S' or anonimato == 'SIM':
                nome = input("Digite o seu nome: ")
                registrar_manifestacoes(conexao, manifestacao, tipo_escolhido, nome)
            elif anonimato == 'N' or anonimato == 'NÃO' or anonimato == 'NAO':
                nome = "Anônimo"
                registrar_manifestacoes(conexao, manifestacao, tipo_escolhido, nome)
            else:
                print("\nValor inválido!\nA manifestação não pôde ser registrada!")
        else:
            print("\nOpção inválida!")


    # 3. PESQUISA UMA MANIFESTAÇÃO PELO CÓDIGO QUE ELA ESTÁ REGISTRADA
    elif opcao_usuario == 3:
        codigo = int(input("Digite o código da manifestação: "))
        pesquisar_manifestacoes(conexao, codigo)

    # 4. ATUALIZA/ALTERA UMA MANIFESTAÇÃO QUE ESTEJA NA LISTA
    elif opcao_usuario == 4:
        lista = ['1', '2', '3', '4', '5']
        tipo = input("Qual o tipo da sua manifestação?\n1) Reclamação\n2) Sugestão\n3) Elogio\n4) Denúncia\n5) Solicitação\nDigite aqui o número correspondente: ")
        if tipo in lista:
            tipo_escolhido = tipo_manifestacao(tipo)
            codigo = int(input("Digite o cógigo da manifestação a ser alterada: "))
            manifestacao_atualizada = input("Digite o texto atualizado: ")
            anonimato = input("Deseja se identificar? (S/N) ").upper()
            if anonimato == 'S' or anonimato == 'SIM':
                nome_manifestante = input("Digite o seu nome: ")
                atualizar_manifestacoes(conexao, codigo, manifestacao_atualizada, tipo_escolhido, nome_manifestante)
            elif anonimato == 'N' or anonimato == 'NÃO' or anonimato == 'NAO':
                nome_manifestante = "Anônimo"
                atualizar_manifestacoes(conexao, codigo, manifestacao_atualizada, tipo_escolhido, nome_manifestante)
            else:
                print("\nValor inválido!\nA manifestação não pôde ser registrada!")
        else:
            print("\nOpção inválida!")

    # 5. REMOVE UMA MANIFESTAÇÃO DA LISTA
    elif opcao_usuario == 5:
        codigo = input("Digite o código da manifestação que será excluída: ")
        remover_manifestacoes(conexao, codigo)

    # 6. EXIBE A QUANTIDADE DE MANIFESTAÇÕES QUE A LISTA POSSUI
    elif opcao_usuario == 6:
        quantidade_manifestacoes(conexao)

    # != 7. PARA QUALQUER VALOR DO MENU QUE NÃO ESTEJAM ENTRE OS NÚMEROS DE 1 A 7
    elif opcao_usuario != 7:
        print("\nOpção inválida!")

    # 7. REALIZA A SAÍDA DO LOOP
    else:
        break

# Encerra a conexão com o Banco de Dados "ouvidoria_testes"!
encerrarConexao(conexao)

print("\nObrigado por utilizar o sistema da Ouvidoria!\nVolte sempre! :)")