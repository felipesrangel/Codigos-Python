num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
if num1 > num2:
    print('\033[0;35mO primeiro número é o \033[1;34mMAIOR')
elif num2 > num1:
    print('\033[0;35mO segundo número é o \033[1;31mMAIOR')
else:
    print('\033[1;36mNão existem número maiores ou menores, são todos iguais.')
