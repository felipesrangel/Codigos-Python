cidade = str(input('Digite o nome de sua cidade: ')).strip()
R = cidade.split()
print('Analisando...')
print('Resultado da análise se sua cidade começa com o nome Santo: {}'.format('SANTO' in R[0].upper()))
