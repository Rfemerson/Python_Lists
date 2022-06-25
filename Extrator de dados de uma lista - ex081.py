lista = []
opcao = ''
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    opcao = str(input('Deseja continuar? [S/N]: '))
    if opcao in 'Nn':
        break
print(f'Foram digitados {len(lista)} valores na lista')
lista.sort(reverse=True)
print(f'Os valores digitado em ordem decrescente foram {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
