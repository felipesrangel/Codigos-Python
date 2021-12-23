n1 = float(input('What is your first mark? '))
n2 = float(input('What is your second mark? '))
arithmetic = (n1 + n2)/2
if arithmetic < 5:
    print('\033[1;31m{}\033[m, It is really bad, I am afraid you are going to repeat this semester.'.format(arithmetic))
elif 5 < arithmetic < 6.9:
    print('\033[1;33m{}\033[m, You will have a second chance to pass in this grade.'.format(arithmetic))
else:
    print('\033[1;34m{}\033[m, You passed!! See you next year.'.format(arithmetic))