from operacoesbd import *


# MENU PRINCIPAL DA OUVIDORIA
def menu():
    print("-" * 30)
    print("     OUVIDORIA UNIFACISA\n\n1. Listar Manifestações \n2. Registrar Manifestações \n3. Pesquisar pelo código \n4. Atualizar uma Manifestação \n5. Remover uma Manifestação \n6. Quantidade de Manifestações \n7. Sair")
    print("-" * 30)

# IMPRIME PARA O USUÁRIO AS OPÇÕES DOS TIPOS DE RECLAMAÇÕES
def tipo_manifestacao(tipo):

    if tipo == '1':
        return "Reclamação"
    elif tipo == '2':
        return "Sugestão"
    elif tipo == '3':
        return "Elogio"
    elif tipo == '4':
        return "Denúncia"
    elif tipo == '5':
        return "Solicitação"

# 1. LISTAR AS MANIFESTAÇÕES
def listar_manifestacoes(conexao):
    manifestacoes = listarBancoDados(conexao, 'select * from manifestacoes;')
    print()
    if len(manifestacoes) > 0:
        for manifestacao in manifestacoes:
            print(f'{manifestacao}')
    else:
        print("Não há manifestações à serem exibidas!")

# 2. REGISTRAR AS MANIFESTAÇÕES
def registrar_manifestacoes(conexao, manifestacao, tipo_escolhido, nome):
    consulta = 'insert into manifestacoes (manifestacao, tipo_manifestacao, nome) values (%s, %s, %s);'
    dados = [manifestacao, tipo_escolhido ,nome]

    registrar = insertNoBancoDados(conexao, consulta, dados)
    print(f'\nManifestação criada com sucesso! Código: {registrar}')

# 3. PESQUISA UMA MANIFESTAÇÃO PELO CÓDIGO QUE ELA ESTÁ REGISTRADA
def pesquisar_manifestacoes(conexao, codigo):
    manifestacoes = listarBancoDados(conexao, f'select * from manifestacoes where codigo = {codigo};')
    print()
    if len(manifestacoes) > 0:
        for manifestacao in manifestacoes:
            print(f'{manifestacao}')
    else:
        print(f"Não há manifestações à serem exibidas para o código: {codigo}!")

# 4. ATUALIZA/ALTERA UMA MANIFESTAÇÃO QUE ESTEJA NA LISTA
def atualizar_manifestacoes(conexao, codigo, manifestacao_atualizada, tipo_escolhido,nome_manifestante):
    consulta = 'update manifestacoes set manifestacao = %s, tipo_manifestacao = %s ,nome = %s where codigo = %s;'
    dados = [manifestacao_atualizada, tipo_escolhido, nome_manifestante, codigo]
    atualiza = atualizarBancoDados(conexao, consulta, dados)

    if atualiza == 1:
        print("\nAtualização realizada com sucesso!")
    else:
        print("\nO código não é válido para atualizações! \nVerifique os códigos existentes na opção: (1. Listar Manifestações)")

# 5. REMOVE UMA MANIFESTAÇÃO DA LISTA
def remover_manifestacoes(conexao, codigo):
    remover = 'delete from manifestacoes where codigo = %s;'
    dados = [codigo]

    linhas_afetadas = excluirBancoDados(conexao, remover, dados)
    print()
    if linhas_afetadas == 0:
        print(f"Nenhuma manifestação foi encontrada no código: {codigo}!")
    else:
        print("Manifestação removida com sucesso!")

# 6. EXIBE A QUANTIDADE DE MANIFESTAÇÕES QUE A LISTA POSSUI
def quantidade_manifestacoes(conexao):
    consulta = 'select count(*) from manifestacoes'
    resultado = listarBancoDados(conexao, consulta)
    print()
    if resultado[0][0] == 1:  # Verifica se a lista possui apenas 1 manifestação
        print(f"O cadastro contém: {resultado[0][0]} manifestação.")  # Reproduz no singular
    else:
        print(f"O cadastro contém: {resultado[0][0]} manifestações.")



