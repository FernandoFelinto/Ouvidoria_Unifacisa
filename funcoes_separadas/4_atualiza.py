from operacoesbd import *

conexao = criarConexao('localhost','root','@BDParticular1992', 'ouvidoria_testes')

codigo = int(input("Digite o cógigo da manifestação a ser alterada: "))
manifestacao_atualizada = input("Digite o texto atualizado: ")
nome_manifestante = input("Digite o nome do manifestante: ")

consulta = 'update manifestacoes set manifestacao = %s, nome = %s where codigo = %s;'
dados = [manifestacao_atualizada, nome_manifestante, codigo]
atualiza = atualizarBancoDados(conexao, consulta, dados)

if atualiza == 1:
    print("\nAtualização realizada com sucesso!")
else:
    print("\nO código não é válido! \nVerifique os códigos existentes na opção: (1. Listar Manifestações)")

encerrarConexao(conexao)