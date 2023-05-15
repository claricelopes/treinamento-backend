
frase = str(input("digite uma frase: ")).strip().upper() 
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for c in range(len(junto) -1, -1, -1):
    inverso += junto[c] 
if inverso == junto: 
    print("é um palíndromo") 
else: 
    print("não é palíndromo") 