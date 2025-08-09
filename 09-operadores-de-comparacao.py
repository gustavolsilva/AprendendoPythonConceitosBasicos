"""
Operadores de comparação: são usados para comparar valores. Eles retornam True ou False.
Os principais operadores de comparação são:
- Igualdade (==) (Para diferenciar o = que é atribuição de variáveis.)
- Desigualdade (!=)
- Maior que (>)
- Menor que (<)
- Maior ou igual a (>=)
- Menor ou igual a (<=)

No if, ele vai executar se o resultado da comparação for True
"""
# %%
from asyncio import sleep


idade = 20
idade < 18 # False
# %%
16 < 18 # True
# %%
True
#%%
False

# %%
4 == 4 # True

# %%
4 != 4 # False
# %%
4 == 4.0 # True
4 == "4" # False

# %%
5 > 10 # False
5 < 10 # True

# %%
5 > 5 # False
5 >= 5 # True

# %%
5 < 5 # False
5 <= 5 # True

# %%
# Minha solução

import time

fome = input("Você está com fome? (s/n) ")
if fome == "s":
    comida_em_casa = input("Você tem comida em casa? (s/n) ")
    if comida_em_casa == "s":
        print("Ótimo! Vamos preparar uma refeição.")
        print(f"{'-'*5}\n")
        time.sleep(5)
        print("Vamos comer!")
        print(f"{'-'*5}\n")
        time.sleep(5)
        print("Satisfeito. Vamos para próxima atividade")
    elif comida_em_casa == "n":
        print("Vamos ao supermercado comprar algo.")
        print(f"{'-'*5}\n")
        time.sleep(5)
        print("Vamos voltar para a casa")
        print(f"{'-'*5}\n")
        time.sleep(5)
        print("Ótimo! Vamos preparar uma refeição.")
        print(f"{'-'*5}\n")
        time.sleep(5)
        print("Vamos comer!")
        print(f"{'-'*5}\n")
        time.sleep(5)
        print("Satisfeito. Vamos para próxima atividade")
    else:
        print("Resposta inválida. Por favor, responda com 's' ou 'n'.")
elif fome == "n":
    print("Que ótimo! Então vamos para a próxima atividade")
else:
    print("Resposta inválida. Por favor, responda com 's' ou 'n'.")

# %%
print("----- INÍCIO -----\n")

resposta1 = input("Estou com fome? (Digite s para sim)")
if resposta1 == "s":
    resposta2 = input("Tenho comida? (Digite s para sim)")
    if resposta2 != "s":
        print("Ir ao mercado")
        print("Voltar para casa")
    print("Preparar uma refeição")
    print("Comer a comida")
print("\n----- FIM -----")

