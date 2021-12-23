tabela = ('Atlético MG', 'Internacional', 'Palmeiras', 'Flamengo', 'Sport Recife',
          'Santos', 'São Paulo', 'Fluminense', 'Vasco da Gama', 'Fortaleza',
          'Atlético GO', 'Atlético PR', 'Ceará SC', 'Corinthians','Grêmio',
          'Bahia', 'Coritiba', 'Bragantino SP', 'Botafogo', 'Goiás')

print('TIMES BRASILERÃO 2020')
print('-='*20)
print(f'Times: {tabela}')
print('-='*20)
print(f'Os cincos primeiros times são: {tabela[0:4]}')
print('-='*20)
print(f'Os quatro últimos colocados são: {tabela[-4:]}')
print('-='*20)
print(f'Time em Ordem Alfabética: {sorted(tabela)}')
print('-='*20)
print(f'O Flamengo está na {tabela.index("Flamengo")+1}ª posição')