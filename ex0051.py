print("="*20)
print("10 TERMOS DE UMA PA")
print("="*20)
t = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
d = t + ( 10 - 1 ) * r
for c in range (t, d, r):
    print("{}".format(c), end= ' -> ')
print('Acabou')
