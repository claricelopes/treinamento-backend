from time import sleep


def contador(i, f, p):
    if p < 0: 
        p*= -1
    if p == 0: 
        p = 1
    print(f'contagem de {i} até {f} contando de {p} em {p}')
    sleep(2.5) 

    if i < f: 
       cont = 1
       while cont <= f: 
           print(f'{cont} ', end='', flush=True) 
           sleep(0.5) 
           cont += p
       print('fim') 
    else:
        cont = i
        while cont >= f: 
            print(f'{cont} ', end='', flush=True) 
            sleep(0.5) 
            cont -= p
        print('fim')


contador(1, 10, 1) 
contador(10, 0, 2) 
print('personalize a contagem: ')
ini = int(input('inicio: '))
fim = int(input('fim: '))
pas = int(input('passo: ')) 
contador(ini, fim, pas)    

