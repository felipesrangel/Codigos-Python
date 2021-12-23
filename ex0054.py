from datetime import date
tot = 0
totm = 0
for c in range (1,8):
    ano = int(input("Em que ano nasceu a {}° pessoa?".format(c)))
    idade = (date.today().year - ano)
    if idade >= 18:
        tot += 1
    else:
        totm += 1
print("Ao todo temos {} pessoas maiores de idade".format(tot))
print("E também tivemos {} pessoas menores de idade".format(totm))
