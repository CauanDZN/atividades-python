soma = cont = 0

while True:
    n = float(input('Digite um número entre 0 e 10: '))
    if n < 0:
        break
    if n > 10:
        break
    cont += 1
    soma += n

print('A soma dos {} valores é igual a {}. ' .format(cont, soma))