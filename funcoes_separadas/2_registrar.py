from operacoesbd import *

conexao = criarConexao('localhost','root','@BDParticular1992', 'ouvidoria_testes')

manifestacao = input("Digite a sua manifestação: ")
anonimato = input("Deseja registrar o seu nome? (S/N) ").upper()

if anonimato == 'S':
    nome = input("Digite o seu nome: ")
elif anonimato != 'N':
    print("Valor inválido!")
else:
    nome = "Anônimo"

consulta = 'insert into manifestacoes (manifestacao, nome) values (%s, %s);'
dados = [manifestacao, nome]

registrar = insertNoBancoDados(conexao , consulta, dados)
print(f'Manifestação criada com sucesso! Código: {registrar}')

encerrarConexao(conexao)