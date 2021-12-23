a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))
if a < b +c and b < a +c and c < a + b:
    print('Com as medidas do lado A {}, B {} e C {} poderemos fazer um triangulo'.format(a, b, c))
else:
    print('Esse triângulo não pode existir')