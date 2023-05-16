
ficha = list()
while True:
    nome = str(input('digite nome: ')) 
    n1 = float(input('digite nota 1: '))
    n2 = float(input('digite nota 2: '))
    media = (n1 + n2) / 2 
    ficha.append([nome, [n1, n2], media])
    resp = str(input('quer continuar? (s/n)'))
    if resp in 'Nn':
        break
print(f'{"No.": >4}{"nome":<10}{"media":>8}') 
for i, a in enumerate(ficha): 
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('mostrar nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('finalizado')
        break 
    if opc <= len(ficha) -1:
        print(f'notas de {ficha[opc] [0]} são {ficha[opc] [1]}') 

 
    