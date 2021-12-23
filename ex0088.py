from time import sleep
from random import randint
print('-'*30)
print('      JOGO DA MEGA SENA      ')
print('-'*30)
n = int(input('Quantos jogos você quer sortear? '))
for c in range (0, n):
    sorteio = [[randint(1,61)], [randint(1,61)], [randint(1,61)],
               [randint(1,61)], [randint(1,61)], [randint(1,61)]]
    sleep(1)
    print(f'Jogo {c+1}: {sorted(sorteio)}')
print('-='*5, '< Boa Sorte >', '-='*5)