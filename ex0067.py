while True:
    n = int(input('Quer ver a taboada de qual valor? '))
    print('-'*33)
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x {c} = {c*n}')
    print('-'*33)
    print('Se quiser encerrar o programar, digite qualquer número negativo.')
print('Programa encerrado!')