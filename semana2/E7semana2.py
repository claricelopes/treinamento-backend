
from random import randint
computador = randint(0, 10)
print("pensei um número, advinhe-o")
acertou = False
tentativas = 0 
while not acertou: 
    jogador = int(input("digite seu palpite: "))
    tentativas = tentativas +1
    if jogador == computador:
        acertou = True
print(f"você acertou com {tentativas} tentativas!") 