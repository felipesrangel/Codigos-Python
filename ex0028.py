from random import randint
from time import sleep
num = int(input('Tente advinhar um número em que estou pensando: '))
escolhido = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if num == escolhido:
    print('{}, Parabéns, você venceu!!'.format(escolhido))
else:
    print('{}, Eu ganhei!!'.format(escolhido))
