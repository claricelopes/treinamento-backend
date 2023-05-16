
valores = [] 
while True:
    valores.append(int(input('digite um valor: ')))
    resp = str(input('quer continuar? [S/N] ')) 
    if resp in 'Nn':
        break
print(f'você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('o valor 5 faz parte da lista')
else:
    print('o valor 5 não faz parte da lista') 