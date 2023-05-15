
ano = int(input("digite o ano que você nasceu: "))
idade = 2023 - ano 

if 18 > idade: 
    print("você ainda irá se alista") 
elif 18 == idade:
    print("é hora de se alistar") 
else: 
    print(f"já se passou {idade - 18} ano(s) do alistamento") 