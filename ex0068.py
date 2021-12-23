from random import randint
c = 0
while True:
    jogador = int(input('Diga um valor: '))
    print('-'*30)
    computador = randint(1, 11)
    lado = ' '
    while lado not in 'PI':
        lado = str(input('Quer par ou ímpar [P/I]? ')).strip().upper()
    print('-'*30)
    resultado = jogador + computador
    print(f'Você jogou {jogador} e o computador jogou {computador}, o resultado foi {resultado}', end= ', ')
    print('DEU PAR' if resultado %2 == 0 else 'DEU ÍMPAR')

    '''PODE ESCREVER O CÓDIGO ASSIM, MAS A FORMA MAIS CURTA PARA MELHORAR É A ORIGINAL
    if resultado % 2 ==0:
        print(f'Você jogou {jogador} e o computador jogou {computador}, o resultado foi {resultado}, DEU PAR')
    else:
        print(f'Você jogou {jogador} e o computador jogou {computador}, o resultado foi {resultado}, DEU ÍMPAR')'''

    if lado == 'P':
        if resultado % 2 == 0:
            c += 1
            print('Você ganhou')
        else:
            print('Computador ganhou')
            break
    if lado == 'I':
        if resultado % 2 != 0:
            c += 1
            print('Você ganhou')
        else:
            print('Computador ganhou')
            break
print('-'*30)
print(f'GAME OVER, você ganhou o total de {c} vezes.')