altura = float(input('Digite um valor: '))
base = float(input('Digite outro valor: '))

area = base * altura
perimetro = base + base + altura + altura

print('O perímetro e área entre {} e {} vale' .format(altura, base))
print('Perímetro =', perimetro)
print('Área =', area)