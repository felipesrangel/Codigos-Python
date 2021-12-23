num = []
for c in range(0, 5):
    num.append(int(input(f'Digite o valor na posição {c}: ')))
print(f'O maior valor é {max(num)} na posição',end=' ')
for i, v in enumerate(num):
    if v == max(num):
        print(i, end='... ')
print(f'\nO menor valor é {min(num)} na posição', end=' ')
for i, v in enumerate(num):
    if v == min(num):
        print(i, end='... ')