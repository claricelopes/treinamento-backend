
while True:
    n = int(input("digite o número que quer ver a tabuada: "))
    if 0 > n: 
        break 
    for c in range(1, 11): 
        print(f"{n} x {c} = {n*c}")  