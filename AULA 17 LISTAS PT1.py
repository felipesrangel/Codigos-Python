''' As tuplas são imutáveis e por isso não pode ser alteradas em nenhum momento, mas existe a forma de solucinar isso
através de listas, utilizando outros comandos.

TUPLAS = ( )

LISTAS = [ ]'''

comida = []
for c in range(0, 5):
    comida.append(str(input('O que o senhor gostaria de pedir? ')))
print('O senhor pediu: ',end='')
for v in comida:
    print(f'{v}', end=' ')
'''
ADICIONANDO ELEMENTOS

Podendo agora modificar o que há dentro da lista, pode ser adicionado elementos nela também, 
utilizando o comando:

comida.append(biscoito) - Adiciona no final
comida.insert(0, biscoito) - Adiciona na posição desejada

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

ELIMINANDO ELEMENTOS

Pode-se eliminar elementos nas listas utilizando:

delcomida[3] - utiliza índice
comida.pop(3) - ''''''''''''' Se não quiser utilizar o índice, pode deixar em branco que vai eliminar o último elemento
comida.remove('biscoito') - Utiliza valores


ORGANIZANDO VALORES

valores.sort() - ordem crescente ou alfabética
valores.sort(reverse=True) - ordem inversa


CÓPIA DE LISTAS

a = (11 , 2, 3, 4)
b = a

No caso acima, você não está copiando "a", você está igualando, ou seja, se mudar "b", vai automaticamente mudar "a".
Para fazer a cópia, utiliza esses comandos:

a = (11, 2, 3, 4)
b = a[:] 
'''


