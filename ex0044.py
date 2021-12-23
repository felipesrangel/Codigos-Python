price = float(input('Purchase prices: R$'))
print('''TYPES OF PAYMENT 
[ 1 ] In cash/check 
[ 2 ] In credit card 
[ 3 ] 2x credit card 
[ 4 ] 3x or more in credit card''')
option = int(input('Wich one do you chose? '))
if option == 1:
    one = price - (price * 10 / 100)
    print('This option has a discount of 10%, you will pay R${:.2f}.'.format(one))
elif option == 2:
    two = price - (price * 5 / 100)
    print('This option has a discount of 5%, you will pay R${:.2f}.'.format(two))
elif option == 3:
    three = price/2
    print('This option has the normal price, you will pay 2x of R${:.2f}.'.format(three))
elif option == 4:
    times = int(input('How many times? '))
    four = (price + (price * 20 / 100))/times
    print('This option has a interest of 20%, you will pay {} of R${:.2f}.'.format(times, four))
else:
    print('This option does not exist')