lista = [[], []]
for c in range(0,7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        lista[0].insert(0, num)
    else:
        lista[1].insert(0, num)
print(f'Os números pares digitados na lista foram {sorted(lista[0])}')
print(f'Os números ímpares digitados na lista foram {sorted(lista[1])}')
