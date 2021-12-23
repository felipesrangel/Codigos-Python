listanum = []
maior = menor = 0
for c in range (0, 5):
    if c == 0:
        n = int(input('Digite um valor: '))
        listanum.append(n)
        print('Adicionado ao final da lista')
    if c == 1:
        n = int(input('Digite um valor: '))
        if n <= listanum[0]:
            listanum.insert(0, n)
            print('Adicionado na posição 0 da lista')
        else:
            listanum.append(n)
            print('Adicionado ao final da lista')
    if c == 2:
        n = int(input('Digite um valor: '))
        if listanum[0] >= n <= listanum[1]:
            listanum.insert(0, n)
            print('Adicionado na posição 0 da lista')
        elif listanum[0] <= n <= listanum [1]:
            listanum.insert(1, n)
            print('Adiconado na posição 1 da lista')
        elif listanum[0] <= n >= listanum[1]:
            listanum.append(n)
            print('Adicionado ao final da lista')
    if c == 3:
        n = int(input('Digite um valor: '))
        if listanum[0] >= n <= listanum[1]:
            listanum.insert(0, n)
            print('Adicionado na posição 0 da lista')
        elif listanum[0] <= n <= listanum[1]:
            listanum.insert(1, n)
            print('Adiconado na posição 1 da lista')
        elif listanum[0] <= n >= listanum[1] and listanum[1] <= n <= listanum[2]:
            listanum.insert(2, n)
            print('Adicionado na posição 2 da lista')
        elif listanum [1] <= n >= listanum [2]:
            listanum.append(n)
            print('Adicionado ao final da lista')
    if c == 4:
        n = int(input('Digite um valor: '))
        if listanum[0] >= n <= listanum[1]:
            listanum.insert(0, n)
            print('Adicionado na posição 0 da lista')
        elif listanum[0] <= n <= listanum [1]:
            listanum.insert(1, n)
            print('Adiconado na posição 1 da lista')
        elif listanum[0] <= n >= listanum[1] and listanum[1] <= n <= listanum[2]:
            listanum.insert(2, n)
            print('Adicionado na posição 2 da lista')
        elif listanum[2] <= n <= listanum [3]:
            listanum.insert(3, n)
            print('Adicionado na posição 3 da lista')
        elif listanum[2] <= n >= listanum[3]:
            listanum.append(n)
            print('Adicionado ao final da lista')
print(listanum)


'''OUTRA FORMA DE FAZER'''

lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos <= len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print(lista)