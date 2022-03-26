an = int(input('Ano de nascimento: '))
aa = 2021
alist = aa - an

print('Quem nasceu em {} tem' .format(an), alist, 'anos em {}.' .format(aa))

if alist < 18:
    print('Faltam apenas', 18 - alist, 'anos para você se alistar para o serviço militar.')
elif alist == 18:
    print('Tá na hora de alistar, futuro soldado!')
else:
    print('Você deverá ter se alistado há', alist - 18, 'ano(s) atrás!')
    print('Seu alistamento foi em', an + 18)
