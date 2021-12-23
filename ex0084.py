dados = list()
pessoas = list()
cont = 0
maiorp = 70
pesados = list()
leves = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    prox = str(input('Deseja cadastrar mais? ')).upper()
    pessoas.append(dados[:])
    dados.clear()
    cont += 1
    if prox == 'N':
        break
ppesados = list()
pleves = list()
for p in pessoas:
    if p[1] > maiorp:
        pesados.append(p[0])
        ppesados.append(p[1])
    if p[1] <= maiorp:
        leves.append(p[0])
        pleves.append(p[1])
print(f'O maior peso foi {ppesados} .Peso de {pesados}')
print(f'O menor peso foi {pleves}.Peso de {leves}')
print(f'Foram cadastradas {cont} pessoas.')

'''OUTRA FORMA'''

dados = list()
pessoas = list()
maiorp = menorp = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorp = menorp = pessoas[1]
    pessoas.append(dados[:])
    dados.clear()
    prox = str(input('Deseja cadastrar mais? ')).upper()
    if prox == 'N':
        break
print(f'O maior peso foi {maiorp} .Peso de ',end='')
for p in pessoas:
    if p[1] == maiorp:
        print(f'{[p[0]]}', end='')
print(f'O menor peso foi {pleves}.Peso de ', end='')
for p in pessoas:
    if p[1] == menorp:
        print(f'{[p[0]]}', end='')
print(f'Foram cadastradas {len(pessoas)} pessoas.')
