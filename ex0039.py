from datetime import date
birth = int(input('When is your birthday? '))
age = (date.today().year - birth)
if age < 18:
    print('\033[1;33mYou only have {} years, don"t have to enlist in the army yet.'.format(age))
elif age == 18:
    print('\033[1;34mIt is time for you to enlist in the army.')
else:
    print('\033[1;31mIt"s passed time to you to enlist in the army, you should do right away!.')