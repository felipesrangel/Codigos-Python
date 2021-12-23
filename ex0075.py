num = int(input('Digite um número: '))
secnum = int(input('Digite outro número: '))
tercnum = int(input('Digite mais um número: '))
ultnum = int(input('Digite o último número: '))
valores = (num, secnum, tercnum, ultnum)
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ',end=' ')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')

'''OUTRA FORMA DE FAZER'''
n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ',end=' ')
for p in valores:
    if p % 2 == 0:
        print(p, end=' ')