def leiaInt(msg):
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m') 
        if ok:
            break
    return valor 


n = leiaInt('digite um número: ')
print(f'você digitou o número {n}')
