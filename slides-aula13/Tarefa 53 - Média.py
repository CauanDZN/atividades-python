n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('Tirando', n1, 'e', n2, ', a média do(a) aluno(a) é', m)

if m < 5.0:
    print('O(a) aluno(a) está reprovado(a).')
elif m >= 5.0 and m < 6.9:
    print('O(a) aluno(a) está de recuperação.')
else:
    print('O(a) aluno(a) está aprovado(a).')
