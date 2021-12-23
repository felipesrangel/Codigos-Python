import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
h = math.hypot(co, ca)
print('\033[0;30mA hipotenusa do triângulo é \33[1;31m{:.2f}'.format(h))
