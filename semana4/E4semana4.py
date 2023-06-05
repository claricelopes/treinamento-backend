def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n) 
    r['maior'] = max(n)
    r['menor'] = min(n) 
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'boa'
        elif r['média'] >= 5:
            r['situação'] = 'razoável'
        else:
            r['situação'] = 'ruim'
    return r 


resp = notas(8.5, 6.0, 3.8, sit=True)   
print(resp) 
