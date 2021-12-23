s = 0
for c in range(1, 7):
    num = int(input('Type the {}° number: '.format(c)))
    if num % 2 == 0:
        s = s + num
print('The sum of all numbers are {}'.format(s))
