def titulo (txt):
    print('-'*20)
    print(txt)
    print('-'*20)
titulo('CONTROLE DE TERRENOS')


def area (a, b):
    area = a * b
    print(f'A área do terreno {a}x{b} é de {area}m²')

area(a=int(input('LARGURA (m)?')), b=int(input('COMPRIMENTO (m)?')))