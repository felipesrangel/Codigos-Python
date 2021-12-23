from datetime import date
nascimento = int(input('DATA DE NASCIMENTO: '))
idade = date.today().year - nascimento
if idade <=9:
    print('\033[0;32mO atleta tem {} anos \n\033[0;35mCLASSIFICAÇÃO \033[1;34mMIRIM'.format(idade))
elif idade <=14:
   print('\033[0;32m O atleta tem {} anos \n\033[0;35mCLASSIFICAÇÃO \033[0;34m INFANTIL'.format(idade))
elif idade <=19:
    print('\033[0;32m O atleta tem {} anos \n\033[0;35mCLASSIFICAÇÃO \033[0;34m JÚNIOR'.format(idade))
elif idade <=25:
    print('\033[0;32m O atleta tem {} anos \n\033[0;35mCLASSIFICAÇÃO \033[0;34m SÊNIOR'.format(idade))
else:
    print('\033[0;32m O atleta tem {} anos \n\033[0;35mCLASSIFICAÇÃO \033[0;34m MASTER'.format(idade))