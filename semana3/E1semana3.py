
num = (int(input('digite um número: ')),
       int(input('digite um número: ')),
       int(input('digite um número: ')),
       int(input('digite um número: ')))
print(f'você digitou os valores {num}')
print(f'o valor 9 apareceu {num.count(9)} vezes') 
if 3 in num:
     print(f'o valor 3 apareceu na posição {num.index(3)+1}')
else:
     print('o valor 3 não apareceu em nunhuma posição')
print('os valores pares digitados foram', end='')
for n in num:
     if n % 2 == 0:
         print(n, end=' ')  





      