def escreva(msg):
    tam = len(msg) 
    print('-' * tam)
    print(f'{msg}') 
    print('-' * tam) 


msg = str(input('digite uma frase: ')) 

escreva(msg) 