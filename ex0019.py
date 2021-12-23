import random
n1 = input('\33[0;31mDigite o nome do(a) aluno(a): ')
n2 = input('\33[0;32mDigite o nome do(a) aluno(a): ')
n3 = input('\33[0;33mDigite o nome do(a) aluno(a): ')
n4 = input('\33[0;34mDigite o nome do(a) aluno(a): ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('\33[0;30mO aluno escolhido foi \33[1;35m{}'.format(escolhido))

