salário = int(input('Qual o seu salário? '))
if salário <= 1250:
    aumento = (salário*(15/100)+salário)
else:
    aumento = (salário*(10/100)+salário)
print('Você ganhará um aumento e passará a ganahr ${:.2f}'.format(aumento))