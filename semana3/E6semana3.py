
temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('digite nome: ')))
    temp.append(float(input('digite o peso:')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1] 
    princ.append(temp[:]) 
    temp.clear()
    resp = str(input('quer continuar? (s/n)'))
    if resp in 'Nn':
        break 
print(f'foram cadastradas {len(princ)} pessoas')
print(f'o maior peso foi de {mai}kg' , end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]')
print(f'o menor peso foi de {men}kg' , end='') 
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]') 