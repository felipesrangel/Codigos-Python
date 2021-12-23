from random import randint
from time import sleep
from operator import itemgetter
sorteio = {'jogador1' : randint(0, 9),
'jogador2' : randint(0, 9),
'jogador3' : randint(0, 9),
'jogador4' : randint(0, 9)}
ranking = list()
print(' VALORES SORTEADOS')
for j, r in sorteio.items():
    print(f'O {j} tirou {r}')
    sleep(1)
print('-='*20)
print('     ==RESULTADOS==')
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')
    sleep(1)