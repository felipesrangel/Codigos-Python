def maior(*num):
    print('Analisando os valores passados...')
    for n in num:
        print(n, end=' ')
    print(f'Foram informados {len(num)} valores ao todo. \nO maior valor informado foi {max(num)}.')
    print('-='*40)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)