from random import randint
cont = maior = menor =0
print(f'Os números sorteados foram:',end=' ')
while cont != 5:
    escolhidos = randint(0,9)
    cont += 1
    print(escolhidos, end=' ')
    if cont == 1:
        maior = menor = escolhidos
    else:
        if escolhidos > maior:
            maior = escolhidos
        if escolhidos < menor:
            menor = escolhidos
print(f'\nO número {maior} é o maior \nO número {menor} é o menor')



'''OUTRA FORMA'''


numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),)
print('Os valores sorteados foram: ',end=' ')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor foi: {max(numeros)}')
print(f'O menor valor foi: {min(numeros)}')