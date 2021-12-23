maior = 0
nomemaior = ''
si = 0
mi = 0
s = 0
for p in range (1, 5):
    print('========== {} PESSOA =========='.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    si += idade
    if sexo == 'M':
        if idade == 1:
            maior = idade
            nomemaior = nome
        else:
            if idade > maior:
                maior = idade
                nomemaior = nome
    if sexo == 'F':
        if idade < 20:
            s += 1
mi = float(si/4)
print('O homem mais velho tem {} anos de idade e seu nome é {}'.format(maior, nomemaior))
print('A média das idades é de {}'.format(mi))
print('Neste lugar possuem {} mulher com menos de 20 anos'.format(s))