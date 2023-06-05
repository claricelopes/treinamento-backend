from musica import Musicas, Spotify 

spt = Spotify()
while True:
    nome = input('digite o nome de uma música: ')
    cant = input('digite o nome do cantor dela: ') 

    musica = Musicas(nome, cant) 

    spt.adicionar_musica(musica)

    perg = input('deseja continuar? ') 


    if perg != 'sim': 
        break 
    
    
spt.mostrar_musicas()  
