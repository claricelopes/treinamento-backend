
listagem = ('tomate', 1.50,
            'alface', 3.0,
            'cebola', 2.0,
            'arroz', 4.50,
            'feijão', 5.0,
            'leite', 8.0,) 
print(f'{"listagem de preços":40}')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}') 