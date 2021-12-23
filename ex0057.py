masculino = 'M'
feminino = 'F'
r = 'M' and 'F'
while r != 'M' and 'F':
    r = str(input('Qual o seu sexo? [M/F]: ')).upper()
    print('Tente novamente!')
print('Obrigado pela sua cooperação!')