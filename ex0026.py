algo = str(input('Digite algo: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(algo.count('A')))
print('A letra A aparece pela primeira vez em {}'.format(algo.find('A')+1))
print('A letra A aparece pela última vez em {}'.format(algo.rfind('A')+1))
