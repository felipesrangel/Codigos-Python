listanum = []
cont = 0
while True:
    n = int(input('Digite um número: '))
    listanum.append(n)
    cont += 1
    prox = str(input('Gostaria de continuar? ')).upper()
    if prox == 'N':
        break
print(f'Lista: {listanum} \nForam digitados {cont} números')
listanum.sort(reverse=True)
print(f'Os valores em ordem descrescente: {listanum}')
if 5 in listanum:
    print('O número 5 está na lista')
else:
    print('O número 5 não foi encontrado na lista.')