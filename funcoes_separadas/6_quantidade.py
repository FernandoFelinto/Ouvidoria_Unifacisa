from operacoesbd import *

conexao = criarConexao('localhost','root','@BDParticular1992', 'ouvidoria_testes')

consulta = 'select count(*) from manifestacoes;'
resultado = listarBancoDados(conexao, consulta)

if resultado[0][0] == 1:  # Verifica se a lista possui apenas 1 manifestação
    print(f"A lista contém: {resultado[0][0]} manifestação.")  # Reproduz no singular
else:
    print(f"A lista contém: {resultado[0][0]} manifestações.")

encerrarConexao(conexao)