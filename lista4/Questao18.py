from math import sqrt

catop = float(input('Comprimento do cateto oposto: '))
cadad = float(input('Comprimento do cateto adjacente: '))

r1 = catop ** 2 + cadad ** 2
h = sqrt(r1)

print('A hipotenusa do triângulo é', round(h, 2))