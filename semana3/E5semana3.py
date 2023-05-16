
num = list()
pares = list()
impares = list()

while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')) 
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
            pares.append(v)
    else:
            impares.append(v) 
print(f'a lista completa é: {num}')
print(f'a lista dos números pares é: {pares}')
print(f'a lista dos números impares: {impares}') 