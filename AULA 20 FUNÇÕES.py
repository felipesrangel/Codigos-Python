'''A utilização de funções pode ser usada para rotinas

Digamos que precise de algo que seja simples e de fácil acesso e personalizado a sua necessidade

para chamarmos essa função, utilizamos o comando:

- def

EX.:
print("------------------------------")
print("           ESCOLA             ")
print("------------------------------")
print("           OLÁ MUNDO          ")
print("------------------------------")
print("           CEV                ")
print("------------------------------")
print("           lUIZ f             ")


Ao invés de escrevermos as 4x o print de linha, podemos fazer uma função onde você só irá
precisar chamar uma única vez e ira fazer do mesmo jeito que está acima.


EX.:
def mostraLinha():
    print("-----------------------------")

mostraLinha()
print("           ESCOLA             ")
mostraLinha()
print("           OLÁ MUNDO          ")
mostraLinha()
print("           CEV                ")
mostraLinha()
print("           lUIZ f             ")

Cada vez que você chamar o mostraLinha, ele vai entrar na função def e irá fazer o que está dentro
do comando que no caso, é mostrar as linhas.'''

print('-'*20)
print('Luiz Felipe')
print('-'*20)
print('Computador')
print('-'*20)
print('CEV')
print('-'*20)

print('-='*30)
def lin():
    print('-'*20)


lin()
print('Luiz Felipe')
lin()
print('Computador')
lin()
print('CEV')
lin()

'''Podendo fazer de forma diferente também, encaixando o que quiser nas funções: '''

def mensagem(msg):
    print('-'*20)
    print(msg)
    print('-'*20)


mensagem('Luiz Felipe')
mensagem('Computador')
mensagem('CEV')

'''Nessa parte, foi criado a função "mensagem" e dentro dela vai receber o "msg"
Quando foi posto "Luiz Felipe" dentro de "mensagem", ele vai ser enviado lá para cima e transformado em "msg"
seguindo direto para o print.

Ex. com números:'''

a = 5
b = 4
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 1
b = 2
s = a + b
print(s)

'''Simplificando com def'''


def soma(a, b):
    s = a + b
    print(s)


soma(5,4)
soma(8,9)
soma(1,2)

'''Colocados os parâmetros A e B, você poderá chamar dois números para fazer as somas,
entretano se adicionar ou retirar os parâmetros, poderá dar erro, pois não está de igual quantidade 
 do que você estabeleceu na função.
 
Outra coisa é identificar na parte da chamada, podendo também inverter:'''
def soma(a, b):
    s = a + b
    print(s)


soma(a=5, b=4)
soma(b=5, a=4)

'''Outros exemplos práticos:'''

print('-='*40)

def contador(*num):
    print(num)

contador(4, 6, 5)
contador(4, 2)
contador(7, 5, 2, 4, 6)

'''Com esse símbolo de *, os números serão empacotados dentro de uma variável "num" 
e serão transformados em uma tupla, esse processo é chamado de EMPACOTAMENTO'''

def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(4, 6, 5)
contador(4, 2)
contador(7, 5, 2, 4, 6)

'''LISTAS COM FUNÇÃO

trabalhando com as listas em uma função def:'''

def dobra(lst):
    pos = 0
    while pos <= len(lst):
        lst[pos] *= 2
        pos += 1

valores = [2, 4, 6, 5]
dobra(valores)
print(valores)

'''Nesse caso criamos duas listas para poder trabalhar com elas de forma correta'''