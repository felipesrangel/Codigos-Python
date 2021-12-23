viagem = float(input('Qual será a distância que percorreremos? '))
if viagem <=200:
    preço = float(viagem*0.50)
else:
    preço = float(viagem*0.45)
print('Sua viagem custará {:.2f}'.format(preço))



