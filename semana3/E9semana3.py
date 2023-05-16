from datetime import datetime
dados = dict()
dados['nome'] = str(input('digite nome: '))
nasc = int(input('digite ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc 
dados['sexo'] = str(input('digite sexo: (M/F): ')) 
dados['ctps'] = int(input('carteira de trabalho: (0, não tem)')) 
if dados ['ctps'] != 0:
    dados['contratação'] = int(input('digite ano de contratação: '))
    dados['salário'] = float(input('digite salário: '))
    if dados['sexo'] == 'Ff':
       dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 30) - datetime.now().year) 
    else:
       dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year) 
for k, v in dados.items():
    print(f' - {k} tem o valor {v}') 