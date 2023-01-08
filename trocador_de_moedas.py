def trocar_moeda(valor):
    global valor2
    valor = valor2
    if 0 <= valor <= 1000000:
        cem = valor // 100
        valor %= 100
        cinquenta = valor // 50
        valor %= 50
        vinte = valor // 20
        valor %= 20
        dez = valor // 10
        valor %= 10
        cinco = valor // 5
        valor %= 5
        dois = valor // 2
        valor %= 2

        um = valor // 1
        valor %= 1
        cinq_cents = valor // 0.50
        valor %= 0.50
        vinte_cinco_cents = valor // 0.25
        valor %= 0.25
        dez_cents = valor // 0.1
        valor %= 0.1
        cinco_cents = valor // 0.05
        valor %= 0.05
        um_cent = valor // 0.01
        valor %= 0.01
    elif valor == '':
        print('Digite um valor válido')
    else:
        print('O Valor deve estar entre 0.01 e 100000')

    print(f'Notas: \n'
          f'{cem} notas de 100 \n'
          f'{cinquenta} notas de 50 \n'
          f'{vinte} notas de 20 \n'
          f'{dez} notas de 10 \n'
          f'{cinco} notas de 5 \n'
          f'{dois} notas de 2 \n'
          f'Moedas: \n'
          f'{um_cent} moedas de 1 \n'
          f'{cinquenta} moedas de 50 \n'
          f'{vinte_cinco_cents} moedas de 25 \n'
          f'{dez_cents} moedas de 10 \n'
          f'{cinco_cents} moedas de 5 \n'
          f'{um_cent} moedas de 1 \n')


try:
    valor2 = float(input('Digite um valor: '))
except ValueError:
    print('Digite um valor válido')
else:
    trocar_moeda(valor2)
