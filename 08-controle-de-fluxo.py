"""
Controle de fluxo: é um conjunto de instruções que permitem tomar decisões no código. De ir para um caminho
ou outro caminho dependendo da condição naquele momento. 
Na vida real, também tomamos decisões com base em condições, como escolher o que vestir com base no clima.

No Python usamos duas palavras: if e else
"""

#%%
idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você tem exatamente 18 anos!")
else:
    print("Você tem mais de 18 anos!")
