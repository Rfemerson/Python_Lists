valorespar = []
valoresimp = []
resp = ''
while True:
    num = int(input('Digite um valor: '))
    resp = str(input('Deseja Continuar? [S/N]: '))
    if num % 2 == 0:
        valorespar.append(num)
    else:
        valoresimp.append(num)
    if resp in 'Nn':
        break
print('=-' * 30)
print(f'Os valores impares digitados foram {valoresimp}')
print(f'Os valores impares difitados foram {valorespar}')
valores = valoresimp + valorespar
valores.sort()
print(f'Os valores digitados foram {valores}')

