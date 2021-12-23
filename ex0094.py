pessoa = {}
grupo = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Responda Somente com M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda somente com S ou N.')
    if resp == 'N':
        break
print('-='*20)
print(f'A) - Foram cadastradas ao todo {len(grupo)}')
media = soma / len(grupo)
print(f'B) - A média de idade é de {media:.2f}')
print('C) - As mulheres que foram cadastradas são', end=' ')
for p in grupo:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('D) - Lista de pessoas que estão acima da idade média: ')
for p in grupo:
    if p['idade'] >= media:
        print(f'    ->{p["nome"]}')
print('>>>>>ENCERRADO<<<<<')