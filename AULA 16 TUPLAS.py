'''VARIÁVEIS COMPOSTAS
Tupla = Variável que abriga mais de um valor = SÃO IMUTÁVEIS

() - TUPLA
[] - LISTA
{} - DICIONÁRIO'''


lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim',)

for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}, na posição {cont}')

for pos, comida in enumerate (lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Nossa, comi pra caramba')

a = (2, 5, 4)
b = (5, 8, 1 , 2)
c = a + b
print(c.count())
'''Count - Acha quantas vezes aparece
    Index - Acha posição'''

pessoa = ('Luiz', 21, 'M', 50.53)
del (pessoa)
'''
Tupla é imutável, entretanto vc pode apaga-la por inteira através do DEL
'''