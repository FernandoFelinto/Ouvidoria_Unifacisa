from operacoesbd import *

conexao = criarConexao('localhost','root','@BDParticular1992', 'ouvidoria_testes')

manifestacoes = listarBancoDados(conexao, 'select * from manifestacoes;')

if len(manifestacoes) > 0:
    for manifestacao in manifestacoes:
        print(f'{manifestacao}')
else:
    print("Não há manifestações à serem exibidas!")

encerrarConexao(conexao)