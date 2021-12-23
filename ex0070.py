print('=-='*7)
print('LOJA COM DESCONTO!!')
print('=-='*7)
preco = milprod = valortot = precobarato = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    cont += 1
    valortot += preco
    if cont == 1 or preco < precobarato:
        barato = produto
        precobarato = preco
    if preco > 1000:
        milprod += 1
    c = ' '
    while c not in 'SsNn':
        c = str(input('Quer continuar? ')).strip().upper()
    if c == 'N':
        break
print(f'\033[30mValor total de compra: \033[30:33m${valortot:.2f} \n\033[30mTotal de produtos que custaram acima de $1000,00: \033[30:35m{milprod} \n\033[30mProduto mais barato foi o \033[32m{barato} \033[30me custou \033[32m${precobarato}')