valores = []
maior = menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print('=-' * 25)
print(f'Os valores digitados foram {valores}')
print(f'O maior valor digitado foi {maior}, na posição ', end='')
for p, v in enumerate(valores):
    if v == maior:
        print(f'...{p}')
print(f'O menor valor digitado foi {menor}, posição ', end='')
for p, v in enumerate(valores):
    if v == menor:
        print(f'...{p}', end=)

