n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))

# Maior
if n1 > n2:
    print('O maior valor digitado foi {}. '.format(n1))
elif n2 > n1:
    print('O maior valor digitado foi {}. '.format(n2))
else:
    print('Os dois números são iguais. ')