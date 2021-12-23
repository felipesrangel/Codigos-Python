s = 0
cont = 0
for c in range(1, 500):
    if c % 3 == 0 and c % 2 == 1:
        cont = cont + 1
        s += c
print('O somatório de todos os {} valores é {}'.format(cont, s))