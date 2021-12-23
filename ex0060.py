from math import factorial
fator = int(input('Qual número deseja saber o fatorial? '))
c = fator + 1
while c != 1:
    c -= 1
    print(' {} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
print(factorial(fator))
print('FIM')

n = int(input('Digite o número para o cálculo de seu fatorial: '))
c = n
f = 1
print('Calculando seu fatorial {}! = '.format(n), end= '')
while c > 0:
    print('{}'.format(c), end= '')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print(f)