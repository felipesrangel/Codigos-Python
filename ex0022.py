nome = str(input('Qual o seu nome?')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('A quantidade de letras que seu nome todo possui são {} letras'.format(len(nome) - nome.count(' ')))
nome = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(nome[0])))

