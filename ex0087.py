matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sp = sc = maior = 0
for c in range(0, 3):
    for l in range(0 ,3):
        matriz[l][c] = int(input(f'Digite um número [{l} ; {c}]: '))
        if matriz[l][c] % 2 == 0:
            sp += matriz[l][c]
        if matriz[0][1] > maior:
            maior = matriz[0][1]
        if matriz[1][1] > maior:
            maior = matriz[1][1]
        if matriz[2][1] > maior:
            maior = matriz[2][1]
sc += matriz[2][0] + matriz[2][1] + matriz[2][2]
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {sp}')
print(f'A soma dos valores da terceira coluna é {sc}')
print(f'O maior valor da segunda linha é {maior}')