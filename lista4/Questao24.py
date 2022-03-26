n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')
n3 = input('Digite o terceiro número: ')

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O maior número digitado é {}. '.format(maior))