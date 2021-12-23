from random import shuffle
n1 = input('Digite primeiro aluno: ')
n2 = input('Digite segundo aluno: ')
n3 = input('Digite terceiro aluno: ')
n4 = input('Digite quarto aluno: ')
alunos = [n1, n2, n3, n4]
shuffle(alunos)
print('As apresentações seguirão a ordem', alunos)




