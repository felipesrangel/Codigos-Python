weight = float(input('Weight (Kg): '))
high = float(input('High (m):'))
imc = weight/high**2
print('The IMC of this person is {:.1f}'.format(imc))
if imc <= 18.5:
    print('This person is Under wight')
elif imc <= 24.9:
    print('This person is Normal weight')
elif imc <= 29.9:
    print('This person is Overweight')
elif imc <= 34.9:
    print('This person is Grade 1 Obesity')
elif imc <= 39.9:
    print('This person is Grade 2 Obesity')
else:
    print('This person is Grade 3 Obesity')