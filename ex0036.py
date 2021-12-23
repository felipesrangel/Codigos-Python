house = float(input('What is the house is price? '))
money = float(input('How much is your salary? '))
time = int(input('In how many years do you inted to pay the house? '))
installment = (house/(time*12))
if (installment) > (money*(30/100)):
    print('\033[0;35m For pay a house that costs ${:.2f} in {} years, the installment will be ${:.2f}. \033[0;30m You \033[1;31m CANNOT \033[0;30m buy this hosue.'.format(house,time, installment ))
else:
    print('\033[1;34m Seria um prazer fazer um empréstimo para essa compra!')

