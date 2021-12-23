print('=-='*8)
print('CADASTRE UMA PESSOA!!')
print('=-='*8)
contidade = conthomen = contmulher = 0
s = ' '
while True:
    i = int(input('Idade: '))
    while s not in 'MmFf':
        s = str(input('Sexo [M/F] ')).strip().upper()
    print('-'*20)
    if i > 18:
        contidade += 1
    elif s == 'M':
        conthomen += 1
    elif s == 'F':
        if i < 20:
            contmulher += 1
    c = ' '
    while c not in 'SsNn':
        c = str(input('Quer continuar? ')).strip().upper()
        print('-'*30)
    if c == 'N':
        break
print(f'No seu cadastro possuem {contidade} maiores de 18, {conthomen} homens de qualquer idade e {contmulher} mulheres com menos de 20 anos')
