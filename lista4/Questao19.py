larg = float(input('Diga a largura da parede: '))
alt = float(input('Diga a altura da parede: '))

area = larg * alt
res = area/2

print('Para uma parede de {}m², serão necessários: {}l de tinta' .format(area, res))