num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Esse valor não pode ser adicionado.')

    prox = str(input('Deseja continuar? [S/N]? '))
    if prox == 'n':
        break
print(sorted(num))
