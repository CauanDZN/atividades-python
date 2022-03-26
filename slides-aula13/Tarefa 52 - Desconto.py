tot = float(input('Qual foi o valor total da compra? R$'))
print('\n------------- RESULTADO -------------')
print('Você comprou R$' , tot, 'na nossa loja. OBRIGADO!')

d = 0.10 * tot

if tot >= 500:
    print('=============== ATENÇÃO ===============')
    print('Por fazer mais de R$500,00 em compras,')
    print('você vai receber R$', round(d, 2), 'de desconto.')
    print('O valor a ser pago será de R$', round(tot - d, 2), '!')
    print('Volte sempre!')
