print('='*20)
print('CAIXA ELETRÔNICO')
print('='*20)
valor = int(input('Qual valor será sacado? '))
total = valor
contced = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        contced += 1
    else:
        if contced > 0:
            print(f'Total de {contced} de cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        contced = 0
        if total == 0:
            break

