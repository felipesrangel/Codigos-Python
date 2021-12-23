s = m = media = maior = menor = 0
r = ' '
while r != 'N':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar [S/N]: ')).upper()
    s += 1
    m = (m + n)
    media = m / s
    if s == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Você digitou {} números e a média entre eles foi {}.'.format(s, media))
print('O maior valor é {} e o menor é {}'.format(maior, menor))