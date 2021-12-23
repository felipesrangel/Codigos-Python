
listagem = ('Abacate', 'Caderno', 'Celular', 'Bolsa', 'Porta',
            'Chifre', 'Borracha', 'Papagaio', 'Mesa', 'Destino')
for p in listagem:
    print(f'\nTemos na palavra {p}', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')