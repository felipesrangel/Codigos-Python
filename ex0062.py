p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = p
cont = 1
total = 0
c = 10
while c != 0:
    total = total + c
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    c = int(input('\nQuantos termos gostaria de adicionar? '))
print('A PA teve o total de {} termos'.format(total))

