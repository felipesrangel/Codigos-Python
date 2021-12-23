from datetime import date
ficha = {}
ficha['nome'] = str(input('Nome: '))
ficha['nascimento'] = int(input('Ano de Nascimento: '))
ficha['idade'] = date.today().year - ficha['nascimento']
ficha['ct'] = int(input('Carteira de Trabalho (0 NÃO POSSUO): '))
del ficha['nascimento']
if ficha['ct'] != 0:
    ficha['contrato'] = int(input('Ano de Contratação: '))
    ficha['salario'] = float(input('Salário: R$'))
    ficha['aposentadoria'] = ficha['idade'] + (ficha['contrato'] + 40) - date.today().year
    print('-='*25)
    for i, n in ficha.items():
        print(f'{i} tem o valor {n}')
else:
    for i, n in ficha.items():
        print(f'{i} tem o valor {n}')