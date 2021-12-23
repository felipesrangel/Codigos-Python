radar = int(input('Qual a sua velocida: '))
multa = (radar-80)*7
if radar <=80:
    print(
        'Mantenha sua velocidade e cuidado para não ir muito rápido.')
else:
    print('MULTADO, você estava indo a {}Km/h ultrapassou os limites da velocidade nessa estrada, terá que pagar ${} reais'.format(radar, multa))


