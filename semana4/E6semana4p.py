def ficha(jog='<desconhecido>', gols=0): 
    print(f'o jogador {jog} fez {gols} gol(s)!')


n = str(input('digite o nome do jogador: '))
g = str(input('digite o número de gol(s): ')) 
if g.isnumeric():
    g = int(g) 
else:
    g = 0
if n.strip == '': 
    ficha(gol=g) 
else: 
    ficha(n, g) 