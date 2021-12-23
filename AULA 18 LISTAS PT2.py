''' Colocar uma lista dentro de uma lista:

pessoas =[[Pedro, 25], [Maria, 19], [João, 17]]

Quando uma lista está dentro de outra, apesar de Pedro ter o índice 0 e 25 ter o índice 1, na lista "pessoas"
 eles JUNTOS vão ter o índice 0. Caso fosse chamar eles seria assim:

pessoas =[[Pedro, 25], [Maria, 19], [João, 17]]

print(pessoas[0][0]

Assim você chamaria na dentro da lista, o índice 0 e dentro desse índice, teria o índice 0 que seria Pedro.

Se fosse chamar os dois, poderia ser somente: PRINT(PESSAOS[0]
Porquê viria: [Pedro, 25]

pessoas =[[Pedro, 25], [Maria, 19], [João, 17]]
print(pessoa[0][0] ----------- Pedro
print(pessoa[1][1] ----------- 19
print(pessoa[2][0] ----------- João
print(pessoas[1]   ----------- [Maria, 19]'''

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 40
galera.append(teste[:])
print(galera)

''' Necessário tomar cuidado quando for trabalhar eese tipo de lista, pq é comum achar que só precisa fazer o .appen(),
mas ATENÇÃO e lembrar de fazer a cópia da lista, para que não haja ligação entre elas e vc possa trabalhar livremente
as duas coisas.'''

print()
gente = [['Gustavo', 25], ['Maria', 43], ['Pedro', 63], ['Livia', 15]]
for p in gente:
    print(f'{p[0]} tem {p[1]} anos de idade')

print()
dado = list()
gente = list()
for d in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    gente.append(dado[:])
    dado.clear()

for i in gente:
    if i[1] >= 21:
        print(f'{i[0]} é maior de idade')
    else:
        print(f'{i[0]} é menor de idade')