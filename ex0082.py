lista = []
pares = lista[:]
impares = lista[:]
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    prox = str(input('Gostaria de continuar? ')).upper()
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    if prox == 'N':
        break
print(f'A lista completa: {lista}')
print(f'Lista dos números pares {pares}')
print(f'Lista dos números ímpares: {impares}')