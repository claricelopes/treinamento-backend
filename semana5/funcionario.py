class Funcionario: 
    def __init__(self, nome, salario): 
        self.nome = nome
        self.salario = salario


    def mostrar_info(self):
        return (f'{self.nome}, {self.salario}') 
    