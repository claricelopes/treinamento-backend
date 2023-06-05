class Musicas: 
    def __init__(self, nome, cantor):
        self.nome = nome
        self.cantor = cantor 


    def mostrar_infos(self):
        print(f'nome: {self.nome}')
        print(f'cantor: {self.cantor}') 


class Spotify: 
    def __init__(self):
        self.lista = []


    def adicionar_musica(self, musica):  
        self.lista.append(musica)  


    def mostrar_musicas(self):
        for e in self.lista:
            print(f'nome: {e.nome}, cantor: {e.cantor}')       
