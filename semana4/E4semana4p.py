from time import sleep 


def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(1) 
        if cont== 0:
            maior = valor 
        else:
            if valor > maior:
                maior = valor 
        cont += 1 
    print(f'foram informados {cont} valores ao todo')
    print(f'o maior valor informado foi {maior}.')  


maior(8, 9, 3, 5, 2, 1)
maior(3, 8, 0)
maior(2, 7)
maior(5)  