from random import randint
from time import sleep
itens = ('Rock', 'Paper', 'Scisors')
computer = randint(0,2)
print('''Your options
[ 0 ] Rock
[ 1 ] Paper
[ 2 ] Scisors''')
player = int(input('Make your choice: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('The computer chose {}'.format(itens[computer]))
print('The Player chose {}'.format(itens[player]))
if computer == 0:
    if player == 0:
        print('TIE GAME')
    elif player == 1:
        print('PLAYER WINS')
    elif player == 2:
        print('COMPUTER WINS')
    else:
        print('Invalid move')
if computer == 1:
    if player == 0:
        print('COMPUTER WINS')
    elif player == 1:
        print('TIE GAME')
    elif player == 2:
        print('PLAYER WINS')
    else:
        print('Invalid move')
if computer == 2:
    if player == 0:
        print('PLAYER WINS')
    elif player == 1:
        print('COMPUTER WINS')
    elif player == 2:
        print('TIE GAME')
    else:
        print('Invalid move')