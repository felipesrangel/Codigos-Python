ficha = dict()
ficha['Nome'] = str(input('Nome: '))
ficha['Média'] = float(input('Média: '))
for k, v in ficha.items():
    print(f'{k} é igual a {v}')
if ficha['Média'] >= 6:
    print('Estudante aprovado')
else:
    print('Estudante reprovado')
