from operacoesbd import *

conexao = criarConexao('localhost','root','@BDParticular1992', 'ouvidoria_testes')

codigo = int(input("Digite o código da manifestação: "))
manifestacoes = listarBancoDados(conexao, f'select * from manifestacoes where codigo = {codigo};')

if len(manifestacoes) > 0:
    for manifestacao in manifestacoes:
        print(f'{manifestacao}')
else:
    print("Não há manifestações à serem exibidas!")

encerrarConexao(conexao)