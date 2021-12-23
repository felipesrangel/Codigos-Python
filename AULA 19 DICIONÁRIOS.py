'''Dicionários são estruturas de dados semelhantes as tuplas e as listas, mas com índices literais

["Pedro", "25"]
Pedro tem índice - 0
25 tem índice - 1

Nos dicionários você pode reconhecer o Pedro como NOME e 25 como IDADE

Simbolo dos dicionários

Dados = {}
Dados = dict()

EX.:
dados = {'nome':'Pedro', 'iadde': 25}
print(dados['nome']) - Pedro
print(dados['idade'] - 25


ADICIONAR DADOS:

Nos dicionários não funciona o comando append, basta você inserir da seguinte maneira:

dados['sexo'] = 'M'


REMOVENDO ELEMENTOS:

Assim como feito anteriormente:

del dados['idade']



Ex.:
filme = {'titulo: 'Star Wars',
         'ano': 1977
        'diretor': 'George Lucas
        }

Se quiser mostrar todos os valores ditados:

print(filme.values()) - Star Wars, 1977, George Lucas
print(filme.keys()) - titulo, ano, diretor
print(filme.items()) - mostra tanto um quanto o outro

for k, v in filme.items():
print(f'O {k} é {v}')

- O {filme} é {Star Wars}
- O {ano} é {1977}
- O {diretor} é {Geroge Lucas}



PODERÁ SER FEITO UM DICIONÁRIO DENTRO DE UMA LISTA:

locadora = [[{'filme': 'Star Wars'},{'ano': 1977}],{'diretor': 'George Lucas'}],
            [{'filme': 'Matrix'},{'ano': 1999}],{'diretor': 'Wachowski'}],
            [{'filme': 'Avengers'},{'ano': 2012}],{'diretor': 'Joss Whedon'}]]
print(locadora[0]['ano']
print(locadora[2]['titulo']'''''

pessoas = {'nome':'Gustavo','sexo':'M', 'idade': 25}
print(pessoas['nome'], pessoas['sexo'], pessoas['idade'])
print()
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos e é de sexo {pessoas["sexo"]}')
print()
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

'''COPIANDO LISTAS E DICIONÁRIOS: '''

estado = dict()
br = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    br.append(estado.copy())
for e in br:
    for v in e.values:
        print(v, end=' ')
    print()