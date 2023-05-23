def voto(ano):
    from datetime import date
    atual = date.today().year 
    idade = atual - ano 
    if idade < 16: 
        print(f'com {idade} anos, o voto é NEGADO')
    elif 16 <= idade <= 17 or idade >= 65:
        print(f'com {idade} anos, o voto é OPCIONAL') 
    else: 
        print(f'com {idade} anos, o voto é OBRIGATÓRIO') 


ano = int(input('digite seu ano de nascimento: '))
voto(ano) 
