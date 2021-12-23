num = int(input('Digite um número inteiro: '))
print('''Escolha a base que deseja fazer a conversão: 
\033[0;35m[ 1 ] Converter para BINÁRIO
\033[0;34m[ 2 ] Converter para OCTAL
\033[0;31m[ 3 ] Converter para HEXADECIMAL\033[m''')
opção = int(input('Digite sua opção: '))
if opção == 1:
    print('\033[1;31m{}\033[m convertido para \033[1;32mBINÁRIO\033[m é igual \033[1;33m{}'.format(num, bin(num)))
elif opção == 2:
    print('\033[1;34m{}\033[m convertido para \033[1;35mOCTAL\033[m é igual \033[1;36m{}'.format(num, oct(num)))
elif opção == 3:
    print('\033[1;37m{}\033[m convertido para \033[1;33mHEXADECIMAL\033[m é igual \033[1;34m{}'.format(num, hex(num)))
else:
    print('\033[4;31mOPÇÃO INVÁLIDA')