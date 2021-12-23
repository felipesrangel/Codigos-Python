ficha = {}
quantgols = list()
totgol = 0
ficha['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantos partidas {ficha["nome"]} jogou? '))
if partidas > 0:
    for c in range(0, partidas):
        quantgols.append(int(input(f'Quantos gols {ficha["nome"]} fez no {c}º jogo? ')))
ficha['gols'] = quantgols[:]
ficha['total de gols'] = sum(quantgols)
print('-='*20)
print(ficha)
print('-='*20)
for i, v in ficha.items():
    print(f'O campo {i} tem valor {v}')
print('-='*20)
print(f'O jogador {ficha["nome"]} jogou {len(ficha["gols"])}')
for i, v in enumerate(ficha['gols']):
    print(f'-> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {ficha["total de gols"]}')