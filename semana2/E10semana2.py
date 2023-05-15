
from random import randint
v = 0
while True:
    jgd = int(input("digite um valor: "))
    cmp = randint(0, 10)
    total = jgd + cmp 
    tipo = " "
    while tipo not in "pi":
        tipo = str(input("Par ou Ímpar? ")).strip()[0]
    print(f"você jogou {jgd} e o computador {cmp}, total de {total}.")
    if tipo == "p": 
        if total % 2 == 0:
            print("você venceu!")
            v +=1 
        else:
            print("você perdeu!") 
            break
    elif tipo == "i":
        if total % 2 == 1:
            print("você venceu!")
            v +=1
        else: 
            print("você perdeu!")
            break
print(f"FIM! você venceu {v} vezes.") 
    



