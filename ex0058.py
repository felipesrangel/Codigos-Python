from random import randint
c = 0
num = (1, 5)
escolhido = randint(1, 6)
while num != escolhido:
    num = int(input('Tente advinhar um número em que estou pensando: '))
    c += 1
    if num != escolhido:
        print('Tente novamente!')
    else:
        print('Você ganhou!')
print('Você precisou de {} tentativas.'.format(c))
