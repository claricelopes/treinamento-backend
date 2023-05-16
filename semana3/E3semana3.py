
num = list() 
while True:
    n = int(input('digite um valor: ')) 
    if n not in num:
        num.append(n)
        print('valor aplicado')
    else:
        print('valor duplicado')
    r = str(input('quer continuar? (s/n): ')) 
    if r in 'Nn':
        break
num.sort()
print(f'você digitou os valores {num}:') 