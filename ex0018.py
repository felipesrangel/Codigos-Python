from math import sin, cos, radians
A = int(input('\33[1;33mDigite o ângulo: '))
seno = sin(radians(A))
cosseno = cos(radians(A))
azul = ('\33[1;34;45m')
vermelho = ('\33[1;31;45m')
fundo = ('\33[1;30;45m')
print('{}O {}seno{} e {}cosseno{} do ângulo {} são, respectivamente, {}{:.2f} e {}{:.2f}\33[m'. format(fundo, azul, fundo, vermelho, fundo, A, azul, seno, vermelho, cosseno))

