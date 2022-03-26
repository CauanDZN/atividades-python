import sys

print('---------------------------')
print('  SUPER TABUADA      ')
print('---------------------------')
print('+      Adição')
print('-       Subtração')
print('*       Multiplicação')
print('/       Divisão')
print('=======================')
op = str(input('Digite sua opção: '))
print('=======================')
if op != '+' and op != '-' and op != '*' and op != '/':
    print('Sinal inválido.')
    sys.exit()
else:
    print('Você escolheu a opção', op)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if op == '+':
    print('Realizando a operação:', n1, '+', n2)
    print('===== PROCESSANDO =====')
    print('Resultado da SOMA é', n1 + n2)
    print('=======================')
elif op == '-':
    print('Realizando a operação:', n1, '-', n2)
    print('===== PROCESSANDO =====')
    print('Resultado da SUBTRAÇÃO é', n1 - n2)
    print('=======================')
elif op == '*':
    print('Realizando a operação:', n1, 'x', n2)
    print('===== PROCESSANDO =====')
    print('Resultado da MULTIPLICAÇÃO é', n1 * n2)
    print('=======================')
else:
    print('Realizando a operação:', n1, '/', n2)
    print('===== PROCESSANDO =====')
    print('Resultado da DIVISÃO é', n1 / n2)
    print('=======================')
