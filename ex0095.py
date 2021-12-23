jogador = {}
time = []
listagols = []
while True:
    jogador.clear()
    listagols.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    q = int(input('Quantas partidas o jogador jogou? '))
    for c in range(0, q):
        listagols.append(int(input(f'Quantos gols {jogador["nome"]} fez na {c+1}º partida? ')))
    jogador['gols'] = listagols[:]
    jogador['Total'] = sum(listagols[:])
    time.append(jogador.copy())
    resp = str(input('Quer continuar [S/N]? ')).upper()[0]
    while resp in 'SN':
        break
    if resp == 'N':
        break
print('-='*35)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end=' ')
print()
print('-'*41)
for i, v in enumerate(time):
    print(f'{i:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end=' ')
    print()
print('-'*41)
print()
while True:
    opc = int(input('Mostrar dados de qual jogador [999 PARA]? '))
    print('-='*20)
    if opc == 999:
        break
    if opc >= len(time):
        print(f'Erro! Não existe jogador com código {opc}')
    else:
        print(f'LEVANTAMENTO DOS DADOS DO JOGADOR {time[opc]["nome"]}')
        for i, v in enumerate(time[opc]['gols']):
            print(f'No jogo {i} fez {v} gols')

