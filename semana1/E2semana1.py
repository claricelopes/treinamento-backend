n1 = int(input("digite um valor: "))
n2 = int(input("digite um valor: "))
n3 = int(input("digite um valor: "))
n4 = int(input("digite um valor: ")) 
n5 = int(input("digite um valor: ")) 

maior = n1 
if n2>n3 and n2>n4 and n2>n5 and n2>n1: 
    maior = n2 
if n3>n1 and n3>n2 and n3>n4 and n3>n5:
    maior = n3 
if n4>n1 and n4>n2 and n4>n3 and n4>n5: 
    maior = n4 
if n5>n1 and n5>n2 and n5>n3 and n5>n4:
    maior = n5 
print("o maior valor digitado foi: {}".format(maior))  