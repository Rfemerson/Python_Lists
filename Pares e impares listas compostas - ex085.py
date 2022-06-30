valores = [[], []]
num = 0
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
print('=*' * 30)
print(f'Os valores pares digitados foram {sorted(valores[0])}')
print(f'Os valores impares digitados foram {sorted(valores[1])}')
