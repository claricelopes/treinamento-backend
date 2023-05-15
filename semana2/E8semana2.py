
resposta = 's'
soma = quantidade = media = maior = menor = 0 
while resposta in 's':
    num = int(input('digite um número: '))
    soma += num 
    quantidade += 1 
    if quantidade == 1: 
        maior = menor = num 
    else: 
        if num > maior: 
            maior = num 
        if num < menor:
            menor = num 
    resposta = str(input('quer continuar? (s/n) ')).strip()  
    media = soma / quantidade
print(f'a média entre os números digitados é: {media}, sendo o maior deles: {maior}, e o menor: {menor}') 
   
   