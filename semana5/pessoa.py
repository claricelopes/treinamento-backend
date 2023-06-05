class Pessoa:  
    def __init__(self,
    nome, idade ): 
        self.nome =  nome
        self.idade = idade


    def mostrar_info(self):
        return f'{self.nome}, {self.idade}' 
 