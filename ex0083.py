eq = str(input('Digite sua equação: '))
lista = []
for simb in eq:
    if simb == '(':
        lista.append('(')
    else:
        if simb == ')':
            if len(lista) > 0:
                lista.pop()
            else:
                lista.append(')')
if len(lista) == 0:
    print('Essa equação pode ser executada.')
else:
    print('Essa equação está com falta de parênteses.')