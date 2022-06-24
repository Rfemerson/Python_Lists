opcao = ''
num = []
while True:
    n = (int(input('Digite um número: ')))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicionar')
    opcao = str(input('Deseja Continuar? S/N: '))
    if opcao in 'Nn':
        print(num)
        break
print('=*' * 30)
print(f'Os valores digitados foram {num.sort()}')

