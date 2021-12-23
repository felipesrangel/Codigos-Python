from time import sleep
maior = 0
menu = 0
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
while menu != 5:
    menu = int(input('O que gostaria de fazer: \n[1] SOMAR \n[2] MULTIPLCIAR \n[3] MAIOR \n[4] NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA \nESCOLHA: '))
    if menu != 5:
        print('PROCESSANDO...')
        sleep(2)
    if menu == 1:
        soma = v1 + v2
        print('A soma dos dois números é {}.'.format(soma))
    elif menu == 2:
        mult = v1 * v2
        print('A multiplicação dos valores é {}.'.format(mult))
    elif menu == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('O {} é o maior'.format(maior))
    elif menu == 4:
        print('Quais números gostaria de adicionar? ')
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o segundo valor: '))
    elif menu == 5:
        print('Finalizando o programa...')
        sleep(2)
        print('Finalizado!!')
    else:
        print('Opção Inválida')
print('Volte sempre!')