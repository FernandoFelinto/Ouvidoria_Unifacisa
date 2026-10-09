from operacoesbd import *

conexao = criarConexao('localhost','root','@BDParticular1992', 'ouvidoria_testes')

codigo = input("Digite o código da manifestação que será excluída: ")
remover = 'delete from manifestacoes where codigo = %s;'
dados = [codigo]

linhas_afetadas = excluirBancoDados(conexao, remover, dados)

if linhas_afetadas == 0:
    print("Nenhuma manifestação foi encontrada!")
else:
    print("Manifestação removida com sucesso!")

encerrarConexao(conexao)