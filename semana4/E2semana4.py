from random import randint
from time import sleep


def sorteia(lista): 
    print('sorteando 5 valores da lista: ') 
    for cont in range(0, 5): 
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('printo')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'soamando os valores pares da {lista}, temos: {soma} ') 

numeros=list()
sorteia=(numeros)  
somaPar=(numeros) 