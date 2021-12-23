preco = ('Lápis',1.75,
          'Caderno',15.90,
          'Borracha',2,
          'Estojo',25,
          'Transferidor',4.20,
          'Compasso',9.99,
          'Mochila',120.32,
          'Canetas',22.30,
          'Livro',34.90)
print('-'*40)
print(f'{"LISTA DE PREÇOS:^40"}')
print('-'*40)
for pos in range (0, len(preco)):
    if pos % 2 == 0:
        print(f'{preco[pos]:.<30}', end='')
    else:
        print(f'{preco[pos]:>7.2f}')