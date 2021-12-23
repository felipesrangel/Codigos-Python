from time import sleep

def contagem (i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')

contagem(1, 10, 1)
contagem(10, 0, 1)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('INÍCIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSO: '))
contagem(inicio, fim, passo)